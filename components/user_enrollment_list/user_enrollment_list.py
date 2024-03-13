from django_components import component

@component.register("user_enrollment_list")
class User_enrollment_list(component.Component):
    template_name = "user_enrollment_list/template.html"

    def get_context_data(self):
        return {
            "param": "sample value",
        }

    class Media:
        css = "user_enrollment_list/style.css"
        js = "user_enrollment_list/script.js"