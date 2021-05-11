# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 18:41:20 2021

@author: Pit
"""

# ФУНКЦИЯ ПРЕОБРАЗОВАНИЯ "ФАМИЛИЯ ИМЯ ОТЧЕСТВО" В "ФАМИЛИЯ И.О."
def FIO(l_name):
    q = 0
    f_name = []
    n_list = l_name.split()
    for i in n_list :
        if q != 0 :
            f_name.append('{io}.'.format(io = i[0]))
        else:
            f_name.append('{io} '.format(io = i))
        q = q + 1
        Fam_I_O = (''.join(f_name))
    return Fam_I_O


# ГРАФИК ЗАРАБОТКА ВОДИТЕЛЯ И ДИСПЕТЧЕРА ЗА ВЕСЬ РАССМАТРИВАЕМЫЙ ПЕРИОД 
import plotly
import plotly.graph_objs as go
import cx_Oracle
# from plotly.offline import iplot

print("\033[H\033[J")
print("Начало построения графика.")
my_list_1 = []
my_list_2 = []
my_avg = []
my_list_dr_1 = []
my_list_dr_2 = []
my_avg_dr = []

l_user = 'MIKHEEV_OA'
l_pass = open(r'C:\Users\Pit\Documents\Conn_To_ORACLE\PSW_MikheevOA.txt', 'r').read()
ip = '13.95.167.129'
port = 1521
dsn = cx_Oracle.makedsn(ip, port, service_name = 'pdb1')
db = cx_Oracle.connect(l_user, l_pass, dsn)

mycursor = db.cursor()
mycursor.execute('SELECT ID_DISPATCHER, DISPATCHER_NAME, INCOME_DISP FROM DISP_EARNINGS')
for record in mycursor.fetchall():
    my_list_1.append('{a} _ ID{b}'.format(a = FIO(record[1]), b = record[0]))
    my_list_2.append(record[2])
    
sum_sal = sum(my_list_2)
avg_sal = round(sum(my_list_2) / len(my_list_2), 2)    

mycursor.execute('SELECT ID_DRIVER, DRIVER_NAME, INCOME_DRIVER FROM DRIVER_EARNINGS')
for record in mycursor.fetchall():
    my_list_dr_1.append('{a} _ ID{b}'.format(a = FIO(record[1]), b = record[0]))
    my_list_dr_2.append(record[2])

sum_sal_dr = sum(my_list_dr_2)
avg_sal_dr = round(sum(my_list_dr_2) / len(my_list_dr_2), 2)    

mycursor.execute('SELECT MIN(APP_DT), MAX(APP_DT) FROM basic_showcase_one')
for record in mycursor.fetchall():
    min_date = record[0]
    max_date = record[1]

l_t = 'Зарплата диспетчера и водителя за весь период c {min_d} по {max_d}.'.format(min_d = min_date.strftime("%d.%m.%Y"), max_d = max_date.strftime("%d.%m.%Y"))    
l_s = 'Суммарная з/п диспетчера: {s}\n р. Средняя з/п диспетчера: {a} р.'.format(s = sum_sal, a = avg_sal)    
l_s_d = 'Суммарная з/п водителя: {s}\n р. Средняя з/п водителя: {a} р.'.format(s = sum_sal_dr, a = avg_sal_dr)    

for i in range(len(my_list_1)) :
    my_avg.append(avg_sal)

for i in range(len(my_list_dr_1)) :
    my_avg_dr.append(avg_sal_dr)

trace1 = go.Scatter(x = my_list_1, y = my_list_2, mode = 'lines+markers', name = 'Зарплата диспетчера')
trace2 = go.Scatter(x = my_list_1, y = my_avg, mode = 'lines', name = 'Средняя зарплата диспетчера')
trace3 = go.Scatter(x = my_list_dr_1, y = my_list_dr_2, mode = 'lines+markers', name = 'Зарплата водителя')
trace4 = go.Scatter(x = my_list_dr_1, y = my_avg_dr, mode = 'lines', name = 'Средняя зарплата водителя')

layout1 = go.Layout(title = l_t, xaxis_title = '{q}  {w}'.format(q = l_s, w = l_s_d), yaxis_title = "Тысяч рублей")
data = [trace1, trace2, trace3, trace4] 
fig = go.Figure(data = data, layout = layout1)
#iplot(fig)
plotly.offline.plot(fig, filename='Зарплата_Диспетчер_и_Водитель.html', auto_open = True)
mycursor.close()
print("Готово.")