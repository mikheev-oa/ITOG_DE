# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:31:36 2021

@author: Pit
"""


# КОЛИЧЕСТВО ПОЕЗДОК И ОЦЕНКА ПОЕЗДКИ КЛИЕНТАМИ НА АВТОМОБИЛЕ ЗА ВЕСЬ ПЕРИОД
import plotly
import plotly.graph_objs as go
import cx_Oracle

print("\033[H\033[J")
print("Начало построения графика.")

my_list_1 = []
my_list_2 = []
my_list_3 = []

m_lst_1 = []
m_lst_2 = []
m_lst_3_2 = []
m_lst_3_3 = []
m_lst_3_4 = []
m_lst_3_5 = []
m_lst_4_2 = []
m_lst_4_3 = []
m_lst_4_4 = []
m_lst_4_5 = []

my_rating_1 = []
my_rating_2 = []
my_rating_3 = []

l_user = 'MIKHEEV_OA'
l_pass = open(r'C:\Users\Pit\Documents\Conn_To_ORACLE\PSW_MikheevOA.txt', 'r').read()
ip = '13.95.167.129'
port = 1521
dsn = cx_Oracle.makedsn(ip, port, service_name = 'pdb1')
db = cx_Oracle.connect(l_user, l_pass, dsn)

mycursor = db.cursor()
mycursor.execute('SELECT MONTH_YEAR_DT, CNT_MONTH_DT, CNT_YEAR_DT FROM COMPL_APP')
for record in mycursor.fetchall():
    my_list_1.append('{a}'.format(a = record[0]))
    my_list_2.append('{b}'.format(b = record[1]))
    my_list_3.append(record[2])

mycursor.execute('SELECT MONTH_DT, YEAR_DT, EVALUATION_TRIP, COUNT(EVALUATION_TRIP) FROM basic_showcase_one GROUP BY EVALUATION_TRIP, MONTH_DT, YEAR_DT ORDER BY YEAR_DT ASC')
for record in mycursor.fetchall():
    m_lst_1.append('{a}'.format(a = record[0]))
    m_lst_2.append('{b}'.format(b = record[1]))
    if record[2] == 2 :  
        m_lst_3_2.append(record[2])
        m_lst_4_2.append(record[3])
    if record[2] == 3 :  
        m_lst_3_3.append(record[2])
        m_lst_4_3.append(record[3])
    if record[2] == 4 :  
        m_lst_3_4.append(record[2])
        m_lst_4_4.append(record[3])
    if record[2] == 5 :  
        m_lst_3_5.append(record[2])
        m_lst_4_5.append(record[3])
    
mycursor.execute('SELECT MONTH_DT, YEAR_DT, EVAL_TRIP FROM number_of_ratings')
for record in mycursor.fetchall():
    my_rating_1.append('{a}'.format(a = record[0]))
    my_rating_2.append('{b}'.format(b = record[1]))
    my_rating_3.append('{c}'.format(c = record[2]))
   
mycursor.execute('SELECT MIN(APP_DT), MAX(APP_DT) FROM basic_showcase_one')
for record in mycursor.fetchall():
    min_date = record[0]
    max_date = record[1]
l_t = 'Количество и оценка поездки за весь период c {min_d} по {max_d}.'.format(min_d = min_date.strftime("%d.%m.%Y"), max_d = max_date.strftime("%d.%m.%Y"))    
l_t_1 = 'Количество поездок автомобилей'.format()

trace0 = go.Bar(x = my_list_1, y = my_list_2, marker = dict(color = 'rgb(102,255,255)'), text = ' поездок', name = l_t_1)
trace1 = go.Scatter(x = my_list_1, y = my_list_2, mode = 'lines+markers', name = 'Количество поездок')
trace2 = go.Scatter(x = my_list_1, y = my_rating_3, mode = 'lines+markers', name = 'Количество оценок (всего)')
trace3 = go.Scatter(x = my_list_1, y = m_lst_4_2, mode = 'lines+markers', name = 'Количество оценок "2"')
trace4 = go.Scatter(x = my_list_1, y = m_lst_4_3, mode = 'lines+markers', name = 'Количество оценок "3"')
trace5 = go.Scatter(x = my_list_1, y = m_lst_4_4, mode = 'lines+markers', name = 'Количество оценок "4"')
trace6 = go.Scatter(x = my_list_1, y = m_lst_4_5, mode = 'lines+markers', name = 'Количество оценок "5"')
  
layout1 = go.Layout(
    title = l_t,
    xaxis_title = 'Месяц и год',
    yaxis_title = "Тысяч рублей")

data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6] 
fig = go.Figure(data = data, layout = layout1)
#iplot(fig)
plotly.offline.plot(fig, filename='Поездки_и_оценка.html', auto_open = True)
mycursor.close()
print("Готово.")