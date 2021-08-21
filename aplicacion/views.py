from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, DetailView,RedirectView, UpdateView, DeleteView, ListView
from .models import Empleado, TiemposAccesso
from .forms import EmpleadoForm
 
# import para manejar el serial

import time
# para el logeo de los usuarios, estas son las funciones basica para las paginas
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin,cls).as_view())

# pagina de inicio
class IndexTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


# pagina para salir del sistema
class LogoutView(RedirectView):
    url = '/login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args,
        **kwargs)


# Pagina para logear al usuario al sistema
class LoginTemplate(FormView):
    template_name = '/login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginTemplate, self).form_valid(form)


# para buscar a un empleado en particular
class SearchView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        value = self.request.GET['query']
        empleados = Empleado.objects.filter(id__contains=value)
        data = [{'data':empleado.id, 'value':empleado.nombre}
        for empleado in empleados]
        suggestions = {'suggestions':data}
        return JsonResponse(suggestions, safe=False)


# estas es la vista para visualizar al empleado
class EmpleadoView(LoginRequiredMixin, DetailView):
    template_name = 'sistema/views.html'
    model = Empleado

class ValidarHuella(LoginRequiredMixin, TemplateView):
    template_name = 'sistema/views.html'
    def get_context_data(self, **kwargs):
        context = super(ValidarHuella,
        self).get_context_data(**kwargs)
        options = "L\n"
        output = ''
        array = None
        error = False
        id_biometrico = -1
        arduinoPort = serial.Serial('/dev/ttyUSB0', 9600,
        timeout=1)
        if arduinoPort.isOpen():
            arduinoPort.close()
        arduinoPort.open()
        time.sleep(1.8)
        arduinoPort.write(options)
        while True:
            try:
                    getSerialValue = arduinoPort.readline()
                    array = getSerialValue.split(':')
                    if len(array) == 2:
                        if str(array[0]) == "success":
                            id_biometrico = array[1].replace('\r\n', '')
                        elif str(array[0]) == "error":  
                            id_biometrico =array[1].replace('\r\n', '')
                            error = True
                        break
                    else:
                            print(getSerialValue)
            except Exception:
                print("hola")
        arduinoPort.close()
        if error:
            context['messagerror'] = array
        else:
            empleado = Empleado.objects.get(id_biometrico=id_biometrico)
            tiempos =TiemposAccesso.objects.filter(empleado_id=empleado, is_open=1)
        if len(tiempos) == 0:
            tiempos =TiemposAccesso(empleado=empleado)
            tiempos.save()
        else:
            tiempos = tiempos[0]
            tiempos.is_open = 0
            tiempos.save()
        context['id_biometrico'] = id_biometrico
        context['object'] = empleado
        context['tiempos'] = tiempos
        context['error'] = error
        return context
# Registrar al empleado al sistema
class RegistrarTemplate(LoginRequiredMixin, FormView):
    form_class = EmpleadoForm
    success_url = 'views'
    template_name = 'sistema/registrar.html'
    def get_context_data(self, **kwargs):
        context = super(RegistrarTemplate,
        self).get_context_data(**kwargs)
        options = "H\n"
        output = ''
        array = None
        error = False
        id_biometrico = -1
        arduinoPort = serial.Serial('/dev/ttyUSB0', 9600,
        timeout=1)
        if arduinoPort.isOpen():
            arduinoPort.close()
        arduinoPort.open()
        time.sleep(1.8)
        arduinoPort.write(options)
        while True:
                try:
                    getSerialValue = arduinoPort.readline()
                    array = getSerialValue.split(':')
                    if len(array) == 2:
                        if str(array[0]) == "success":
                            id_biometrico =array[1].replace('\r\n', '')
                        elif str(array[0]) == "error":
                            id_biometrico =array[1].replace('\r\n', '')#
                            error = True
                        break
                    else:
                        if len(getSerialValue) > 0 :
                            print(getSerialValue)
                except Exception:
                    print("error")
        arduinoPort.close()
        context['id_biometrico'] = id_biometrico
        context['error'] = error
        return context
    def form_valid(self, form):
        id_biometrico = self.request.POST['id_biometrico']
        empleado = form.save(commit=False)
        empleado.id_biometrico = id_biometrico
        empleado.save()
        url_redirect = '%s/%s' % (self.get_success_url(),
        empleado.id)
        return HttpResponseRedirect(url_redirect)

class EditView(LoginRequiredMixin, UpdateView):
    model = Empleado
    success_url = '/view'
    template_name = 'aplicacion/editar.html'
    fields = ['nombre', 'nup','isss', 'telefono','escuela',
    'cargo','tipo_contratacion']
    def form_valid(self, form):
        self.success_url = "/views/%s" % (self.get_object().id)
        return super(EditView, self).form_valid(form)
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'aplicacion/confirm.delete.html'
    success_url = '/'
    def delete(self, request, *args, **kwargs):
        array = None
        options = "D" + str(self.get_object().id_biometrico) + "\n"
        arduinoPort = serial.Serial('/dev/ttyUSB0', 9600,
        timeout=1)
        if arduinoPort.isOpen():
            arduinoPort.close()
        arduinoPort.open()
        time.sleep(1.8)
        arduinoPort.write(options)
        while True:
            getSerialValue = arduinoPort.readline()
            print(getSerialValue)
            array = getSerialValue.split(":")
            if len(array) == 2:
                break
        ids = array[1].replace('\r\n', '')
        if( ids == '1' ):
            return super(DeleteView, self).delete(request,*args, **kwargs)
        else:
            return HttpResponseRedirect('/')
# Vista para paginar los empleados
class EmpleadoPage(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'sistema/paginator_empleado.html'
    context_object_name = 'empleado_list'
    paginate_by = 10
