# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:02:58 2021

@author: Pit
"""

# ФУНКЦИЯ ПРЕОБРАЗОВАНИЯ "ФАМИЛИЯ ИМЯ ОТЧЕСТВО" В "ФАМИЛИЯ И.О."
def FIO(l_name):
    q = 0
    f_name = []
    n_list = l_name.split()
    for i in n_list :
        if q != 0 :
            # f_name.append(i[0] + '.')
            f_name.append('{io}.'.format(io = i[0]))
        else:
            # f_name.append(i + ' ')
            f_name.append('{io} '.format(io = i))
        q = q + 1
        Fam_I_O = (''.join(f_name))
    return Fam_I_O
#==================================================================
    
import plotly
import plotly.graph_objects as go  
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
mycursor.execute('SELECT ID_DRIVER, DRIVER_NAME, AVG(AVG_RAT) FROM avg_ratings GROUP BY ID_DRIVER, DRIVER_NAME ORDER BY ID_DRIVER')

s = 0
for record in mycursor.fetchall():
    my_list_1.append('{a}'.format(a = record[0]))
    my_list_2.append('{b}_{a}'.format(b = FIO(record[1]), a = record[0]))
    my_list_3.append('{c}'.format(c = float(record[2])))
    s = s + float(record[2])

for i in my_list_3 :
    my_list_4.append('{d}'.format(d = s / len(my_list_3)))

mycursor.execute('SELECT MIN(APP_DT), MAX(APP_DT) FROM basic_showcase_one')
for record in mycursor.fetchall():
    min_date = record[0]
    max_date = record[1]
l_t = 'Средняя оценка работы водителя за весь период c {min_d} по {max_d}.'.format(min_d = min_date.strftime("%d.%m.%Y"), max_d = max_date.strftime("%d.%m.%Y"))

trace1 = go.Scatter(x = my_list_2, y = my_list_3, mode = 'lines+markers', name = 'Оценка сотрудника')
trace2 = go.Scatter(x = my_list_2, y = my_list_4, mode = 'lines', name = 'Средняя оценка всех сотрудников')

layout1 = go.Layout(title = l_t, xaxis_title = 'ФИО_ID сотрудника', yaxis_title = 'Средняя оценка сотрудника')
data1=[trace1, trace2]  

fig = go.Figure(data = data1, layout = layout1)
plotly.offline.plot(fig, filename='Средняя_оценка_водителя.html', auto_open = True)
mycursor.close()
print("Готово.") 