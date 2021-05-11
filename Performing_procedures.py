# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 12:41:50 2021

@author: Pit
"""


# Выполнение процедур в Oracle
import cx_Oracle as ora

l_table_name_1 = 'basic_showcase_one'
l_table_name_2 = 'basic_showcase_two'
l_table_name_3 = 'compl_app'
l_table_name_4 = 'basic_car_revenue'
l_table_name_5 = 'disp_earnings'
l_table_name_6 = 'driver_earnings'
l_table_name_7 = 'repair_costs_car'
l_table_name_8 = 'number_of_ratings'
l_table_name_9 = 'avg_ratings'


# подключение к oracle
l_user = 'MIKHEEV_OA'
l_pass = open(r'C:\Users\Pit\Documents\Conn_To_ORACLE\PSW_MikheevOA.txt', 'r').read() 
l_tns = ora.makedsn('13.95.167.129', 1521, service_name = 'pdb1')
l_conn_ora = ora.connect(l_user, l_pass, l_tns)

print("\033[H\033[J")
curs = l_conn_ora.cursor()
print('Начало процесса обновления данных в таблице "{l_t_n_1}"...'.format(l_t_n_1 = l_table_name_1))
curs.execute('DECLARE BEGIN MIKHEEV_OA_basic_showcase_one;  END;')
curs.close()
print('Данные в таблице "{l_t_n_1}" успешно обновлены.'.format(l_t_n_1 = l_table_name_1))
    
print('Начало процесса обновления данных в таблице "{l_t_n_2}"...'.format(l_t_n_2 = l_table_name_2))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_basic_showcase_two;  END;')
curs.close()
print('Данные в таблице "{l_t_n_2}" успешно обновлены.'.format(l_t_n_2 = l_table_name_2))

print('Начало процесса обновления данных в таблице "{l_t_n_3}"...'.format(l_t_n_3 = l_table_name_3))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_compl_app;  END;')
curs.close()
print('Данные в таблице "{l_t_n_3}" успешно обновлены.'.format(l_t_n_3 = l_table_name_3))

print('Начало процесса обновления данных в таблице "{l_t_n_4}"...'.format(l_t_n_4 = l_table_name_4))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_basic_car_revenue;  END;')
curs.close()
print('Данные в таблице "{l_t_n_4}" успешно обновлены.'.format(l_t_n_4 = l_table_name_4))

print('Начало процесса обновления данных в таблице "{l_t_n_5}"...'.format(l_t_n_5 = l_table_name_5))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_disp_earnings;  END;')
curs.close()
print('Данные в таблице "{l_t_n_5}" успешно обновлены.'.format(l_t_n_5 = l_table_name_5))

print('Начало процесса обновления данных в таблице "{l_t_n_6}"...'.format(l_t_n_6 = l_table_name_6))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_driver_earnings;  END;')
curs.close()
print('Данные в таблице "{l_t_n_6}" успешно обновлены.'.format(l_t_n_6 = l_table_name_6))

print('Начало процесса обновления данных в таблице "{l_t_n_7}"...'.format(l_t_n_7 = l_table_name_7))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_repair_costs_car;  END;')
curs.close()
print('Данные в таблице "{l_t_n_7}" успешно обновлены.'.format(l_t_n_7 = l_table_name_7))

print('Начало процесса обновления данных в таблице "{l_t_n_8}"...'.format(l_t_n_8 = l_table_name_8))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_number_of_ratings;  END;')
curs.close()
print('Данные в таблице "{l_t_n_8}" успешно обновлены.'.format(l_t_n_8 = l_table_name_8))

print('Начало процесса обновления данных в таблице "{l_t_n_9}"...'.format(l_t_n_9 = l_table_name_9))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN MIKHEEV_OA_avg_ratings;  END;')
curs.close()
print('Данные в таблице "{l_t_n_9}" успешно обновлены.'.format(l_t_n_9 = l_table_name_9))

print('Готово.')
