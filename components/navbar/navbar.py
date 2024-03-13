from django_components import component

@component.register("navbar")
class Navbar(component.Component):
    template_name = "navbar/navbar.html"