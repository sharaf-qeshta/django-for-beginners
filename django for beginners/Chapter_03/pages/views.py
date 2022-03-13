from django.views.generic import TemplateView


# Class-based views better than normal views
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
