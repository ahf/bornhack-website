from django import template

register = template.Library()


def _resolve_app_name(func):
    if hasattr(func, "view_class"):
        resolved_appname = func.view_class.__module__.split(".")[0]
    else:
        resolved_appname = func.__module__.split(".")[0]
    return resolved_appname


@register.simple_tag(takes_context=True)
def menubuttonclass(context, appname):
    resolved_appname = _resolve_app_name(context["request"].resolver_match.func)

    if appname == resolved_appname:
        return "btn-primary"
    else:
        return "btn-default"


@register.simple_tag(takes_context=True)
def menudropdownclass(context, appname):
    resolved_appname = _resolve_app_name(context["request"].resolver_match.func)

    if appname == resolved_appname:
        return "active"
