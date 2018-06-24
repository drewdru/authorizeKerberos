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

def get_params(app_conf):
    while(True):
        answer = input('Использовать настройки из файла config.py для оставшихся параметров или ввести вручную? [1-2]: ')
        if answer == '1':
            if 'DOMAIN' not in app_conf:
                app_conf['DOMAIN'] = config.app_conf['DOMAIN']
            if 'DNS_LIST' not in app_conf:
                app_conf['DNS_LIST'] = config.app_conf['DNS_LIST']
            if 'HOSTNAME' not in app_conf:
                app_conf['HOSTNAME'] = config.app_conf['HOSTNAME']
            if 'TIME_SERVER' not in app_conf:
                app_conf['TIME_SERVER'] = config.app_conf['TIME_SERVER']
            if 'IS_AUTO_RESOLV' not in app_conf:
                app_conf['IS_AUTO_RESOLV'] = config.app_conf['IS_AUTO_RESOLV']
            if 'IS_DHCP' not in app_conf:
                app_conf['IS_DHCP'] = config.app_conf['IS_DHCP']
        elif answer == '2':
            if 'DOMAIN' not in app_conf:
                app_conf['DOMAIN'] = input('Домен для входа (example.com): ')
            if 'DNS_LIST' not in app_conf:
                app_conf['DNS_LIST'] = get_DNS_LIST()
            if 'HOSTNAME' not in app_conf:
                app_conf['HOSTNAME'] = input('HOSTNAME данного компьютера (smbsrv01): ')
            if 'TIME_SERVER' not in app_conf:
                app_conf['TIME_SERVER'] = input('Сервер для автоматической синхронизации времени (dc.domain.com): ')
            if 'IS_AUTO_RESOLV' not in app_conf:
                app_conf['IS_AUTO_RESOLV'] = ask_yes_or_no('Поддерживает ли сервер автоматическое создание файла resolv.conf?')
            if 'IS_DHCP' not in app_conf:
                app_conf['IS_DHCP'] = ask_yes_or_no('IP-адрес динамический и присваивается DHCP сервером?')
        else:
            print('Ошибка ввода!')
            print('Введите 1, чтобы использовать настройки из файла config.py')
            print('Введите 2, чтобы ввести параметры вручную')
            continue
        return app_conf