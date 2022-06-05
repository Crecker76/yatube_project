from django import template
# В template.Library зарегистрированы все встроенные теги и фильтры шаблонов
# добавляем к ним и наш фильтр
register = template.Library()

@register.filter # декоратор меняющий поведение функции
def addclass(field, css):
    return field.as_widget(attrs={'class': css})