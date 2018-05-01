from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from .models import Book
from .forms import BookForm
from django.http import HttpResponse, Http404

# here are the TemplateViews
from django.views.generic.base import TemplateView,TemplateResponseMixin,ContextMixin

# here are the generic views
from django.views.generic import DetailView,ListView

# here are the generic Edit views
from django.views.generic.edit import CreateView,UpdateView,DeleteView





# Make here your custom mixins classes
class LoginRequiredMixin_mine(object):
    @classmethod
    def as_view(cls,**kwargs):
        view = super(LoginRequiredMixin_mine,cls).as_view(**kwargs)
        return login_required(view)

# here are the  Generic Views.
class BookDetail(DetailView):
    # set up your model here
    model = Book


class BookList(ListView):
    model = Book
    # ther is no need for context here object is sent automatically
    # def get_context_data(self,**kwargs):
    #     context= super(BookList,self).get_context_data(**kwargs)
    #     return context
    def  get_queryset(self,*args,**kwargs):
        qs = super(BookList,self).get_queryset(*args,**kwargs).order_by("-timestamp")
        #.filter(title__startswith='A')
        print(qs)
        return qs



# here are the generic Edit Views.

# you mus specify the form to add the data
class BookCreate(CreateView):
    template_name="forms.html"
    form_class = BookForm

    def form_valid(self,form):
        print(form.instance)
        form.instance.added_by=self.request.user
        return super(BookCreate,self).form_valid(form)


    def  get_success_url(self,**kwargs):
        return reverse('book_list')



class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name="forms.html"



class BookDelete(DeleteView):
    model = Book

    def  get_success_url(self,**kwargs):
        return reverse('book_list')








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
