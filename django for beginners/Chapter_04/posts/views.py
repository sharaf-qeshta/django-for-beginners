from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):  # we use ListView instead of TemplateView because we have data to list
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'  # instead of 'object_list' to make things clear
