from django import relative_url_templates

@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all values of "arg" from the String!
    """
    return value.replace(arg,'')

register.filter('cut',cut)
