from django_components import component

@component.register("not_found")
class Not_found(component.Component):
    template_name = "not_found/template.html"

    def get_context_data(self, item):
        return {
            "item": item,
        }

    class Media:
        css = "not_found/style.css"
        js = "not_found/script.js"