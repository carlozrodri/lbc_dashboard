from lbcapi import api

hmac_key = "a44c1e3130b8416f08844cd0f4027aff"
hmac_secret = "973bf02eedfdb3c870f1456697e7f9bfa4ed1e7aa1e27c4a06771cf946d1d0d5"
conn = api.hmac(hmac_key, hmac_secret)

def get_price_uk():
    x = conn.call('GET', '/buy-bitcoins-online/GBP/national-bank-transfer/.json').json()
    x2 = x['data']['ad_list'][0:20]
    return x2

def get_price_ves():
    x = conn.call('GET', '/sell-bitcoins-online/VED/transfers-with-specific-bank/.json').json()
    x2 = x['data']['ad_list'][0:20]   
    return x2


def get_average_price_uk():
    x = conn.call('GET', '/buy-bitcoins-online/GBP/national-bank-transfer/.json').json()
    x2 = x['data']['ad_list'][0:10]
    sumprice = 0
    for price in range(len(x2)):
        sumprice = sumprice + float(x2[price]['data']['temp_price'])
        average_price = sumprice / len(x2)
    return("{:,.2f}".format(average_price))

def get_average_price_ves():
    x = conn.call('GET', '/sell-bitcoins-online/VED/transfers-with-specific-bank/.json').json()
    x2 = x['data']['ad_list'][6:7]
    sumprice = 0
    for price in range(len(x2)):
        sumprice = sumprice + float(x2[price]['data']['temp_price'])
        average_price = sumprice / len(x2)
    return("{:,.2f}".format(average_price))
    

def get_my_info():
    x = conn.call('GET', '/api/myself/').json()
    x2 = x['data']
    return x2

def getAccountInfo(username):
        return conn.call('GET', '/api/account_info/' + username + '/').json()


def get_average_price_uk2():
    x = conn.call('GET', '/buy-bitcoins-online/GBP/national-bank-transfer/.json').json()
    x2 = x['data']['ad_list'][0:2]
    sumprice = 0
    for price in range(len(x2)):
        sumprice = sumprice + float(x2[price]['data']['temp_price'])
        average_price = sumprice / len(x2)
    return(average_price)

def get_average_price_ves2():
    x = conn.call('GET', '/sell-bitcoins-online/VED/transfers-with-specific-bank/.json').json()
    x2 = x['data']['ad_list'][6:7]
    sumprice = 0
    for price in range(len(x2)):
        sumprice = sumprice + float(x2[price]['data']['temp_price'])
        average_price = sumprice / len(x2)
    return(average_price)

def get_average_any_currency(moneda):
    x = conn.call('GET', '/sell-bitcoins-online/'+ moneda +'/transfers-with-specific-bank/.json').json()
    x2 = x['data']['ad_list'][0:10]
    sumprice = 0
    for price in range(len(x2)):
        sumprice = sumprice + float(x2[price]['data']['temp_price'])
        average_price = sumprice / len(x2)
    return(average_price)


from .models import Bitcoinpriceves, Bitcoinpriceuk
#print(get_average_any_currency("USD"))

def amount_to_get(amount):
    amount_to_send = float(amount)
    btcpriceuk = str(Bitcoinpriceuk.objects.last())
    btcpriceves = str(Bitcoinpriceves.objects.last())
    cantidad_de_btc = amount_to_send / float(btcpriceuk)
    btcpriceresult = float(btcpriceves) * cantidad_de_btc
    res = float(btcpriceresult)
    res2 = "{:,.2f}".format(res)
    return(res)
btcpriceuk = Bitcoinpriceuk.objects.last()
btcpriceves = Bitcoinpriceves.objects.last()
print(type(btcpriceuk))
xs = str(btcpriceves)
xca = float(xs)
print(xca)
print(type(xca))
