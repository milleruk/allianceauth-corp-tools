from django.utils.safestring import mark_safe
from django.template.defaulttags import register

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg

@register.filter(name='deslug')
def deslug(slugged):
    try:
        return slugged.replace('_', ' ')
    except:
        return slugged

@register.filter(name='level')
def skill_level(active, trained):
    alt_text = "Level %d" % active
    omega_dif = trained-active
    full = '<span class="fas fa-circle"></span> '
    alpha = '<span class="fas fa-circle text-danger"></span> '
    empty = '<span class="far fa-circle"></span> '

    return mark_safe('<div role="text" aria-label="{}">{}{}{}</div>'.format(alt_text ,full*active, alpha*omega_dif, empty*(5-(active+omega_dif))))
