
from celery import shared_task
from todolist.services import get_average_price_uk
from .models import Bitcoinpriceuk, Bitcoinpriceves
from celery.decorators import periodic_task
from datetime import timedelta
from .services import get_average_price_uk2, get_average_price_ves2
from celery.schedules import crontab

#@shared_task
#def create_test_object(name):
#    TestModel.objects.create(name=name)



@periodic_task(run_every=timedelta(seconds=55))
def get_price_uk_tasks(): 
    price_uk = get_average_price_uk2()
    price_ves = get_average_price_ves2()

    modelo = Bitcoinpriceuk(priceuk=price_uk)
    modelo2 = Bitcoinpriceves(priceves=price_ves)
    modelo.save()    
    modelo2.save()
