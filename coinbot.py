import json
import requests
import time

gbp_url = "https://api.coindesk.com/v1/bpi/currentprice/GBP.json"
eur_url = "https://api.coindesk.com/v1/bpi/currentprice/EUR.json"

def check_value(value):
    if(value < 1):
        return True
    elif(value > 1 & value - 0.07 <= 1):
        return True
    return False

def get_value(string):
    aux = string.split(',')
    aux = aux[0] + aux[1]
    return float(aux)
    

def send_msg(eur_gbp_value):
    return

def main_loop():
    request = requests.get(gbp_url)
    results_gbp = request.json()

    request = requests.get(eur_url)
    results_eur = request.json()
    
    gbp_rate = get_value(results_gbp['bpi']['GBP']['rate'])
    eur_rate = get_value(results_eur['bpi']['EUR']['rate'])
    eur_gbp_value = eur_rate/gbp_rate
    if(check_value(eur_gbp_value)):
        send_msg(eur_gbp_value)
    print(eur_gbp_value)
    time.sleep(5)
    main_loop()

if __name__ == '__main__':
    main_loop()