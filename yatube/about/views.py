from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    """ Класс для обработки статической страницы автора """
    

    template_name = 'about/author.html'

class AboutTechView(TemplateView):
    """Класс для обработки статической страницы техники"""


    template_name = 'about/tech.html' 