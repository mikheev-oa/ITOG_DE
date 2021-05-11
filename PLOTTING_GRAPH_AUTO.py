# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:17:00 2021

@author: Pit
"""



# ГРАФИК ЗАТРАТ НА ОБСЛУЖИВАНИЕ АВТОМОБИЛЯ ЗА ВЕСЬ РАССМАТРИВАЕМЫЙ ПЕРИОД 
import plotly
import plotly.graph_objs as go
import cx_Oracle

print("\033[H\033[J")
print("Начало построения графика.")
my_list_1 = []
my_list_2 = []
my_list_3 = []
my_list_4 = []

l_user = 'MIKHEEV_OA'
l_pass = open(r'C:\Users\Pit\Documents\Conn_To_ORACLE\PSW_MikheevOA.txt', 'r').read()
ip = '13.95.167.129'
port = 1521
dsn = cx_Oracle.makedsn(ip, port, service_name = 'pdb1')
db = cx_Oracle.connect(l_user, l_pass, dsn)

mycursor = db.cursor()
mycursor.execute('SELECT CAR_BRAND, CNT_CAR, PRC_SERVICE, AVG_CHECK FROM REPAIR_COSTS_CAR')
for record in mycursor.fetchall():
    my_list_1.append('{a} ({b} автом.).'.format(a = record[0], b = record[1]))
    # my_list_2.append(record[1])
    my_list_3.append(record[2])
    my_list_4.append(record[3])
    
mycursor.execute('SELECT MIN(APP_DT), MAX(APP_DT) FROM basic_showcase_one')
for record in mycursor.fetchall():
    min_date = record[0]
    max_date = record[1]
l_t = 'Затраты на техническое обслуживание автомобиля за весь период c {min_d} по {max_d}.'.format(min_d = min_date.strftime("%d.%m.%Y"), max_d = max_date.strftime("%d.%m.%Y"))    

trace1 = go.Scatter(x = my_list_1, y = my_list_3, mode = 'lines+markers', name = 'Суммарные затраты')
trace2 = go.Scatter(x = my_list_1, y = my_list_4, mode = 'lines+markers', name = 'Средние затраты на 1 автомобиль')

layout1 = go.Layout(
   title = l_t,
   xaxis_title = 'Марка автомобиля',
   yaxis_title = "Тысяч рублей")

data = [trace1, trace2] 
fig = go.Figure(data = data, layout = layout1)
#iplot(fig)
plotly.offline.plot(fig, filename='Обслуживание_автомобилей.html', auto_open = True)
mycursor.close()
print("Готово.")