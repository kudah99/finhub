from typing import Optional
import unicodedata
from django import forms

from django.contrib.admin.forms import (
    AdminPasswordChangeForm as BaseAdminOwnPasswordChangeForm,
)
from django.contrib.auth.forms import (
    AdminPasswordChangeForm as BaseAdminPasswordChangeForm,
)
from django.utils.text import capfirst
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .widgets import  INPUT_CLASSES
from .models import Student

UserModel = get_user_model()




class UsernameField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if self.max_length is not None and len(value) > self.max_length:
            # Normalization can increase the string length (e.g.
            # "ﬀ" -> "ff", "½" -> "1⁄2") but cannot reduce it, so there is no
            # point in normalizing invalid data. Moreover, Unicode
            # normalization is very slow on Windows and can be a DoS attack
            # vector.
            return value
        return unicodedata.normalize("NFKC", value)

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "username",
        }

class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = " ".join(INPUT_CLASSES)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields["username"].max_length = username_max_length
        self.fields["username"].widget.attrs["maxlength"] = username_max_length
        if self.fields["username"].label is None:
            self.fields["username"].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"username": self.username_field.verbose_name},
        )



class RegisterForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": False}))
    password1 = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=True,
        label=_("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        label=_("Password confirmation"),
        help_text=_("Enter the same password as before, for verification."),
        strip=True)

    class Meta:
        model = User
        fields = ("username","email","first_name","last_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = " ".join(INPUT_CLASSES)
            #visible.field.widget.attrs['placeholder'] = f"Enter {visible.field.label}"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        Student.objects.create(
                user=user
            )
        return user

class UserChangeForm(BaseUserChangeForm):
    def __init__(
        self,
        request: Optional[HttpRequest] = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(request, *args, **kwargs)

        self.fields["password"].help_text = _(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}" class="text-primary-600 underline whitespace-nowrap dark:text-primary-500">this form</a>.'
        )

        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format("../password/")


class AdminPasswordChangeForm(BaseAdminPasswordChangeForm):
    def __init__(
        self,
        request: Optional[HttpRequest] = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(request, *args, **kwargs)

        self.fields["password1"].widget.attrs["class"] = " ".join(INPUT_CLASSES)
        self.fields["password2"].widget.attrs["class"] = " ".join(INPUT_CLASSES)


class AdminOwnPasswordChangeForm(BaseAdminOwnPasswordChangeForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(kwargs.pop("user"), *args, **kwargs)

        self.fields["old_password"].widget.attrs["class"] = " ".join(INPUT_CLASSES)
        self.fields["new_password1"].widget.attrs["class"] = " ".join(INPUT_CLASSES)
        self.fields["new_password2"].widget.attrs["class"] = " ".join(INPUT_CLASSES)
