from django.shortcuts import render
from django.views.generic.base import TemplateView,TemplateResponseMixin,ContextMixin
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator

# Make here your custom mixins classes
class LoginRequiredMixin_mine(object):
    @classmethod
    def as_view(cls,**kwargs):
        view = super(LoginRequiredMixin_mine,cls).as_view(**kwargs)
        return login_required(view)


class DashBoardTemplateView(LoginRequiredMixin_mine,TemplateView):

    template_name='about.html'

    # The context
    def get_context_data(self,*args,**kwargs):
        context = super(DashBoardTemplateView,self).get_context_data(*args,**kwargs)
        context["title"]= "this is the title"
        return context

class Myview(LoginRequiredMixin_mine,TemplateResponseMixin,ContextMixin,View):


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title']='Some Other Title ;)'
        return self.render_to_response(context)

#  To sum up :
#  @method_decorator(login_required) // will work on the specified method only
#  if you put it over the dispatch() // will work on the class itself
#  Then you can make your won Mixin // the mixin must be the first argument in the class
#  or :
#  override the dispatch() method in your custom mixin class and add the method_decorator(login_required)
#  in it
#  Then:
#  use your class as a mixin
