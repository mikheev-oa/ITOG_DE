# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:30:19 2021

@author: Pit
"""




# Очистка таблиц в Oracle перед загрузкой данных за другой период
import cx_Oracle as ora

l_table_name_1 = 'price_kilometer'
l_table_name_2 = 'drivers_lst'
l_table_name_3 = 'application_service'
l_table_name_4 = 'dispatcher'
l_table_name_5 = 'automobil'
l_table_name_6 = 'maintenance_prc'
l_table_name_7 = 'app_licat'
l_table_name_8 = 'price_distinct'
l_table_name_9 = 'area_distance'
l_table_name_10 = 'consumption_price'

# подключение к oracle
l_user = 'MIKHEEV_OA'
l_pass = open(r'C:\Users\Pit\Documents\Conn_To_ORACLE\PSW_MikheevOA.txt', 'r').read() 
l_tns = ora.makedsn('13.95.167.129', 1521, service_name = 'pdb1')
l_conn_ora = ora.connect(l_user, l_pass, l_tns)

print("\033[H\033[J")

curs = l_conn_ora.cursor()
print('Удаление данных в таблице "{l_t_n_1}"...'.format(l_t_n_1 = l_table_name_1))
curs.execute('DECLARE BEGIN DELETE FROM price_kilometer; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_1}" успешно удалены.'.format(l_t_n_1 = l_table_name_1))

curs = l_conn_ora.cursor()
print('Удаление данных в таблице "{l_t_n_2}"...'.format(l_t_n_2 = l_table_name_2))
curs.execute('DECLARE BEGIN DELETE FROM drivers_lst; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_2}" успешно удалены.'.format(l_t_n_2 = l_table_name_2))

print('НУдаление данных в таблице "{l_t_n_3}"...'.format(l_t_n_3 = l_table_name_3))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN DELETE FROM application_service; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_3}" успешно удалены.'.format(l_t_n_3 = l_table_name_3))

print('Удаление данных в таблице "{l_t_n_4}"...'.format(l_t_n_4 = l_table_name_4))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN DELETE FROM dispatcher; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_4}" успешно удалены.'.format(l_t_n_4 = l_table_name_4))

print('Удаление данных в таблице "{l_t_n_5}"...'.format(l_t_n_5 = l_table_name_5))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN DELETE FROM automobil; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_5}" успешно удалены.'.format(l_t_n_5 = l_table_name_5))

print('Удаление данных в таблице "{l_t_n_6}"...'.format(l_t_n_6 = l_table_name_6))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN DELETE FROM maintenance_prc; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_6}" успешно удалены.'.format(l_t_n_6 = l_table_name_6))

print('Удаление данных в таблице "{l_t_n_7}"...'.format(l_t_n_7 = l_table_name_7))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN DELETE FROM app_licat; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_7}" успешно удалены.'.format(l_t_n_7 = l_table_name_7))

print('Удаление данных в таблице "{l_t_n_8}"...'.format(l_t_n_8 = l_table_name_8))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN DELETE FROM price_distinct; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_8}" успешно удалены.'.format(l_t_n_8 = l_table_name_8))

print('Удаление данных в таблице "{l_t_n_9}"...'.format(l_t_n_9 = l_table_name_9))
curs = l_conn_ora.cursor()
curs.execute('DECLARE BEGIN DELETE FROM area_distance; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_9}" успешно удалены.'.format(l_t_n_9 = l_table_name_9))

curs = l_conn_ora.cursor()
print('Удаление данных в таблице "{l_t_n_10}"...'.format(l_t_n_10 = l_table_name_10))
curs.execute('DECLARE BEGIN DELETE FROM consumption_price; COMMIT; END;')
curs.close()
print('Данные в таблице "{l_t_n_10}" успешно удалены.'.format(l_t_n_10 = l_table_name_10))

print('Готово.')
