
from celery import shared_task
from todolist.services import get_average_price_uk
from .models import Bitcoinpriceuk, Bitcoinpriceves, Listas
from celery.decorators import periodic_task
from datetime import timedelta
from .services import get_average_price_uk2, get_average_price_ves2
from celery.schedules import crontab
from lbcapi import api
hmac_key = "a44c1e3130b8416f08844cd0f4027aff"
hmac_secret = "973bf02eedfdb3c870f1456697e7f9bfa4ed1e7aa1e27c4a06771cf946d1d0d5"
conn = api.hmac(hmac_key, hmac_secret)

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
    x = conn.call('GET', '/sell-bitcoins-online/VED/transfers-with-specific-bank/.json').json()
    data = x['data']['ad_list'][0:20]
    usernames = []
    for price in range(len(data)):
        usernames = data[price]['data']['profile']['username']
        temp_prices = data[price]['data']['temp_price']
        max_amount_availables = data[price]['data']['max_amount_available']
        username_model = Listas(username=usernames, temp_price=temp_prices, max_amount_available=max_amount_availables)
        username_model.save()
        print(usernames)

