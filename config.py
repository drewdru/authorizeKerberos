app_conf = {
    'DOMAIN': 'domain.com', # домен для входа
    'DNS_LIST': [
        {
            'host': 'dc', # DNS сервер домена
            'ip': '192.168.0.1', # IP адрес
            'is_admin_server': True # является первичным DNS сервером домена
        },
        {
            'host': 'dc2', # DNS сервер домена
            'ip': '192.168.0.2' # IP адрес
        },
    ],
    'HOSTNAME': 'smbsrv01', # HOSTNAME данного компьютера
    'TIME_SERVER': 'dc.domain.com', # Сервер для автоматической синхронизации 

    'IS_AUTO_RESOLV': False, # Поддерживает ли сервер автоматическое создание файла resolv.conf?
    'IS_DHCP': False, # IP-адрес динамический и присваивается DHCP сервером?
}