from django_components import component

@component.register("coarse")
class Coarse(component.Component):
    template_name = "coarse/template.html"

    def get_context_data(self):
        return {
            "param": "sample value",
        }

    class Media:
        css = "coarse/style.css"
        js = "coarse/script.js"