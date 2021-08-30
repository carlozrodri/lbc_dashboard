# Create your views here.
from django.shortcuts import redirect, render, HttpResponse
from .forms import TaskForm
from .models import Task
from .services import get_price_uk, get_price_ves, get_average_price_uk, get_average_price_ves, get_average_price_uk2, get_average_price_ves2
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    tasks = Task.objects.all() # add this
    return render(request, "index.html", {"task_form": form, "tasks": tasks})

'''''
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
    #    "precio_uk": get_price_uk(),
   #     "average_uk": get_average_price_uk(),
  #      "precio_ves": get_price_ves(),
 #       "average_ves": get_average_price_ves(),
    }
    return render(request, 'index.html', context)
'''

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

"""""
def multiplication(request):

    num1 = request.POST['num1']
  #  num2 = request.POST['num2']
    

    if num1.isdigit(): #and num2.isdigit():
      #cantidad a mandar
        amount_to_send = int(num1)
        btcpriceuk = get_average_price_uk2()
        btcpriceves = get_average_price_ves2()
        cantidad_de_btc = amount_to_send / float(btcpriceuk)
        btcpriceresult = float(btcpriceves) * cantidad_de_btc

        res = float(btcpriceresult)

        return render(request, "index.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "index.html", {"result": res})
"""