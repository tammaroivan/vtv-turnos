import requests
from bs4 import BeautifulSoup
import re
import time

while(True):
    centro=['Lomas',42] 
    payload = {'type': 'VEHÍCULO_HASTA_2500KG', 'centro': centro[1],'dominio':'AAA000', 'nombre':'Ivan', 'apellido':'Tammaro','telefono':'00000000','celular':'00000000','email':'tammaroivan@gmail.com'}
    r = requests.post("http://200.41.235.148", params=payload) #Request al servidor de la VTV
    soup = BeautifulSoup(r.text, 'html.parser')
    turnos=soup.findAll('td', id=re.compile('^td')) #Obtengo la tabla HTML con los turnos
    print("En "+str(centro[0]))
    if len(turnos)>0: #Si se encontraron turnos
        for turno in turnos: #Recorro los turnos
            dia = int(turno.find('p').get_text()) #Obtengo el dia del turno
            fecha=turno.get('id')[2:].zfill(8) #Obtengo la fecha del turno
            print('Hay turnos el dia '+str(fecha[:2])+'/'+str(fecha[2:4])+'/'+str(fecha[4:8])) #Muestro que dia hay disponible turnos
    else:
        print("No hay turnos") 
    print("---------------------")
    #Espero 7 segundos para buscar nuevamente los turnos disponibles
    time.sleep(7)
