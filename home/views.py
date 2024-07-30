from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView



class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        del self.request.session['name']
        print(self.request.session.get('name', 'farzad'))
        return context
        
    