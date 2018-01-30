import requests
from bs4 import BeautifulSoup
import re
import time

while(True):
    centro=['Lomas',42]
    payload = {'type': 'VEHÍCULO_HASTA_2500KG', 'centro': centro[1],'dominio':'AAA000', 'nombre':'Ivan', 'apellido':'Tammaro','telefono':'00000000','celular':'00000000','email':'tammaroivan@gmail.com'}
    r = requests.post("http://200.41.235.148", params=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    turnos=soup.findAll('td', id=re.compile('^td'))
    print("En "+str(centro[0]))
    if len(turnos)>0:
        for turno in turnos:
            dia = int(turno.find('p').get_text())
            fecha=turno.get('id')[2:].zfill(8)
            print('Hay turnos el dia '+str(fecha[:2])+'/'+str(fecha[2:4])+'/'+str(fecha[4:8])) 
    else:
        print("No hay turnos") 
    print("---------------------")
    time.sleep(7)