from django.contrib import admin, messages
from django.shortcuts import redirect, render
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import context
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView,RedirectView, UpdateView, DeleteView, ListView,View,CreateView
#from django.views.generic.edit import CreateView
from .models import Queja
from .forms import QuejaForm


class FormularioQueja(View):
    def get(self,request,*args,**kwargs):
        form=QuejaForm()
        contexto ={
            'form':form,
        }
        return render (request,'queja.html',contexto)

    def post(self,request,*args,**kwargs):
        
        form=QuejaForm(request.POST)
        
        messages.success(request,'¡QUEJA GENERADA!')
        if form.is_valid():
            form.save()
            return redirect('admin:index')
        else:
            contexto ={
                'form':form,
            }
            return render(request,'queja.html',contexto)

class QuejaList (ListView):
    model=Queja
    template_name='quejalist.html'




class quejaCreateView(CreateView):
   
    model=Queja
    #fields=['DesQueja']
    form_class=QuejaForm
    template_name='queja.html'
    success_url=reverse_lazy('erp:list_queja')
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']= 'FORMULARIO QUEJA'        
        return context