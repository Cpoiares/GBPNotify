from twilio.rest import Client
import json
import requests
import time

'''
Por muito cringe que isto seja foi apenas uma simplificacao criada por mera necessidade, ate me diverti
'''

gbp_url = "https://api.coindesk.com/v1/bpi/currentprice/GBP.json"
eur_url = "https://api.coindesk.com/v1/bpi/currentprice/EUR.json"
accountSid = 'AC3eb64f569aa98aaf3b9d2e78160c2602'
authToken = 'db2735f8b71f144e7f7eeecc4106de61'

twilioClient = Client(accountSid, authToken)
myNumber = '441668932047'
destNumber = '447305665218'

def check_value(value):
    if(value < 1):
        return True
    elif((value > 1) & (value - 0.07 <= 1)):
        return True
    return False

def get_value(string):
    aux = string.split(',')
    aux = aux[0] + aux[1]
    return float(aux)
    
def send_msg(eur_gbp_value):
    message = 'OLHA AI O PREÇO DA POUND MPT: %0.5f\n TROCA AI!!!' % (eur_gbp_value) 
    print("Sending Text... %s\n" % message)
    myMessage = twilioClient.messages.create(body = message, from_=myNumber, to=destNumber)
    print("Text Sent %s - %s\n" % (myMessage.sid, myMessage.body))
    
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
    print('CURRENT VALUE - %0.5f\n' % eur_gbp_value)
    time.sleep(500)
    main_loop()

if __name__ == '__main__':
    main_loop()
