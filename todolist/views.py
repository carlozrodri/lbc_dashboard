# Create your views here.
import django
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic.base import ContextMixin, TemplateView
from .forms import TaskForm, PrecioForm
from django.views.generic.edit import FormView,UpdateView,CreateView,UpdateView
from .models import Task, ValorIntroducido, Resultados
from django.urls import reverse_lazy
from .services import get_price_uk, get_price_ves, get_average_price_uk, get_average_price_ves, get_average_price_uk2, get_average_price_ves2
# Create your views here.
   

def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    tasks = Task.objects.all()
    context = {
        "task_form": form, 
        "tasks": tasks,
        "precio_uk": get_price_uk(),
        "average_uk": get_average_price_uk(),
        "precio_ves": get_price_ves(),
        "average_ves": get_average_price_ves(),
    }
    return render(request, 'index.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "update_task.html", {"task_edit_form": form})
    
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")


def multiplication(request):

    num1 = request.POST['num1']
    p = ValorIntroducido(precio=num1)
    p.save()

    if num1.isdigit(): #and num2.isdigit():
       
        #cantidad a mandar
        amount_to_send = int(num1)
        btcpriceuk = get_average_price_uk2()
        btcpriceves = get_average_price_ves2()
        cantidad_de_btc = amount_to_send / float(btcpriceuk)
        btcpriceresult = float(btcpriceves) * cantidad_de_btc

        res = float(btcpriceresult)
        res2 = "{:,.2f}".format(res)
        modelo = Resultados(resultado=res)
        modelo.save()
        context = {
            "precio_uk": get_price_uk(),
            "average_uk": get_average_price_uk(),
            "result" : res2,
            # "precio_form" : precio2,
            }
        return render(request,"index.html", context)
    else:
        context = {
            "precio_uk": get_price_uk(),
            "average_uk": get_average_price_uk(),
            
        }
        return render(request, "index.html", context)
