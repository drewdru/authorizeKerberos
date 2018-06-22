#!./env/bin/python
# -*- coding: utf-8 -*-
import config

def ask_yes_or_no(question):
    answer_yes = ['y', 'д', '1']
    answer_no = ['n', 'н', '0']
    bool_answer = True
    while(True):
        is_admin_answer = input('{} [y/n/д/н/0/1]: '.format(question)).lower()
        if is_admin_answer in answer_yes:
            break
        elif is_admin_answer in answer_no:
            bool_answer = False
            break
        else:
            print('Ошибка ввода! допустимый ответ: y, n, д, н, 0 или 1')
    return bool_answer

def get_DNS_LIST():
    DNS_LIST = []
    is_havent_admin_server = True
    while(True):
        print('Добавление DNS сервера')
        host = input('Имя DNS сервер домена (dc): ')
        ip = input('IP адрес DNS сервера (192.168.0.1): ')
        is_admin_server = False
        if is_havent_admin_server:
            is_admin_server = ask_yes_or_no('Является ли первичным DNS сервером домена?')
            is_havent_admin_server = False
        DNS_LIST.append({
            'host': host,
            'ip': ip,
            'is_admin_server': is_admin_server
        })
        is_add_DNS = ask_yes_or_no('Добавить ещё один DNS сервер?')
        if not is_add_DNS:
            break
    return DNS_LIST
    

def get_params():
    while(True):
        answer = input('Использовать настройки из файла config.py или ввести вручную? [1-2]: ')
        if answer == '1':
            return config.app_conf
        elif answer == '2':
            DOMAIN = input('Домен для входа (example.com): ')
            DNS_LIST = get_DNS_LIST()
            HOSTNAME = input('HOSTNAME данного компьютера (smbsrv01): ')
            TIME_SERVER = input('Сервер для автоматической синхронизации времени (dc.domain.com): ')
            IS_AUTO_RESOLV = ask_yes_or_no('Поддерживает ли сервер автоматическое создание файла resolv.conf?')
            IS_DHCP = ask_yes_or_no('IP-адрес динамический и присваивается DHCP сервером?')
            return {
                'DOMAIN': DOMAIN,
                'DNS_LIST': DNS_LIST,
                'HOSTNAME': HOSTNAME,
                'TIME_SERVER': TIME_SERVER,
                'IS_AUTO_RESOLV': IS_AUTO_RESOLV,
                'IS_DHCP': IS_DHCP
            }
        else:
            print('Ошибка ввода!')
            print('Введите 1, чтобы использовать настройки из файла config.py')
            print('Введите 2, чтобы ввести параметры вручную')