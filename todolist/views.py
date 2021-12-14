# Create your views here.
import django
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic.base import ContextMixin, TemplateView
from .forms import TaskForm
from django.views.generic.edit import FormView,UpdateView,CreateView,UpdateView
from .models import Task, ValorIntroducido, Resultados
from django.urls import reverse_lazy
from .services import get_price_uk, get_price_ves, get_average_price_uk, get_average_price_ves, get_average_price_uk2, get_average_price_ves2, amount_to_get
from .models import Bitcoinpriceves, Bitcoinpriceuk


# Create your views here.
   
def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    tasks = Task.objects.all()
    
    if 'num1' in request.POST:
        num1 = request.POST['num1']
        p = ValorIntroducido(precio=num1)
        p.save()
        #cantidad a mandar
        res = float(amount_to_get(num1))
        
        modelo = ValorIntroducido(resultado=res)
        modelo.save()
        res2 = Resultados.objects.last()
        res3 = "{:,.2f}".format(res)
        num1_conte = ValorIntroducido.objects.last()

        context = {
        "task_form": form, 
        "tasks": tasks, 
        "result" : res3,
        'inputvalue' : num1_conte,
    }
        return render(request,"index.html", context)
    else:
        context = {
            "task_form": form, 
            "tasks": tasks,
            "precio_uk": get_price_uk(),
            "average_uk": str(Bitcoinpriceuk.objects.last()),
            "precio_ves": get_price_ves(),
            "average_ves": str(Bitcoinpriceves.objects.last()),
            "average_uk_js": str(Bitcoinpriceuk.objects.last()),
            "average_ves_js": str(Bitcoinpriceves.objects.last()),
        }
        return render(request, "index.html", context)




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
