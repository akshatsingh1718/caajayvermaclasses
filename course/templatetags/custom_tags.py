from django import template

register = template.Library()


@register.simple_tag
def active_class(request, url_name):
    """
    Returns 'active' if the request path matches the given url_name.
    """
    return "active" if request.path == url_name else ""
