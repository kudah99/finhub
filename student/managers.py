# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import gettext_lazy as _ 

# def create_user(self,email,password,**extra_fields):

#     if not email:
#         raise ValueError(_("Email is required!"))
#     email = self.normalize_email(email)
#     user = self.model(email=email,is_student= True,**extra_fields)
#     user.set_password(password)
#     user.save()

#     return user