from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .services import get_recipes_with_cache as get_recipes
from .services import get_recipes_without_cache
from datetime import datetime
from django.views.generic import TemplateView,View
from django.contrib import messages
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

#@cache_page(CACHE_TTL)
def recipes_view(request):
    return render(request, 'recipes.html', {'recipes': get_recipes_without_cache()})

class ShowTimeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'show_time.html' 
        print('Users message functon')
        now= datetime.now()
        messages.info(request, 'hello name is hassan')#Storing Message in message backend here
        return render(request, template_name, {'now': now})

def testing_view_func(request):
    print('Hello testing function called here...')
    