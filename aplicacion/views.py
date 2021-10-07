from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, DetailView,RedirectView, UpdateView, DeleteView, ListView,View
from django.views.generic.base import View
from .forms import QuejaForm


class FormularioQueja(View):
    def get(self,request,*args,**kwargs):
        form=QuejaForm()
        contexto ={
            'form':form,
        }
        return render (request,'queja.html',contexto)