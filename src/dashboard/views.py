from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class DashBoardTemplateView(TemplateView):

    template_name='about.html'


    # The context
    def get_context_data(self,*args,**kwargs):
        context = super(DashBoardTemplateView,self).get_context_data(*args,**kwargs)
        context["title"]= "this is the title"
        return context