from django import template

register = template.Library()

@register.inclusion_tag('stroll/walk_element.html')
def walk_element(walk, display_type):
    return {"walk": walk, "display_type": display_type}
