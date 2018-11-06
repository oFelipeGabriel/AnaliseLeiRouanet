import requests
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tipos = []
quantTipos = []

totalUrl = 'http://api.salic.cultura.gov.br/v1/projetos/?format=json&'
res = requests.get(totalUrl)
res = json.loads(res.content.decode('utf-8'))
tot=res['total']
tPaginas = int(tot/100)

url = 'http://api.salic.cultura.gov.br/v1/projetos/?offset='
url2 = '&format=json&'
totalAprovado = 0
totalSolicitado = 0
for x in range(0,10):
    res = requests.get(url+str(x*100)+url2)
    res = json.loads(res.content.decode('utf-8'))
    for d in range(0, 100):
        if(res['_embedded']['projetos'][d]['ano_projeto']=='18'):
            nome = projeto = res['_embedded']['projetos'][d]['nome']
            projeto = res['_embedded']['projetos'][d]['area']
            if(projeto not in tipos):
                tipos.append(projeto)
                quantTipos.append(1)
            else:
                z = tipos.index(projeto)
                quantTipos[z] += 1
            valorAprovado = res['_embedded']['projetos'][d]['valor_projeto']
            valorSolicitado = res['_embedded']['projetos'][d]['valor_projeto']
            print("ID: ",d+(x*100-100))
            print(nome)
            print(projeto)
            totalSolicitado+=float(valorSolicitado)
            totalAprovado+=float(valorAprovado)
            print("%.2f" %valorAprovado)
            print("%.2f" %valorSolicitado)
print("Total solicitado: %.2f" %totalSolicitado)
print("Total Aprovado: %.2f" %totalAprovado)
print(tipos)
print(quantTipos)
#x_axis = range(len(quantTipos))
plt.bar(tipos,quantTipos,width=0.5, color='yellow')
plt.tick_params(length=3,labelsize=6,colors='r',
               grid_color='r', grid_alpha=0.5)


plt.show()


  
