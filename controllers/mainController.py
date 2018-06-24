#!./env/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

from PyQt5.QtCore import QObject, pyqtSlot, QDir, QCoreApplication
from PyQt5.QtQml import QJSValue
from authorizeKerberos import change_configs

class MainController(QObject):
    """ Controller for main view """
    def __init__(self, app_dir=None):
        QObject.__init__(self)
        self.app_dir = QDir.currentPath() if app_dir is None else app_dir
        self.callback = []

    @pyqtSlot(bool, bool, str, list, str, str)
    def update_configs(self, is_auto_resolv, is_dhcp, domain, 
            dns_list, hostname, time_server):        
        change_configs.update({
            'DOMAIN': domain,
            'DNS_LIST': dns_list,
            'HOSTNAME': hostname, # HOSTNAME данного компьютера
            'TIME_SERVER': time_server, # Сервер для автоматической синхронизации 
            'IS_AUTO_RESOLV': is_auto_resolv, # Поддерживает ли сервер автоматическое создание файла resolv.conf?
            'IS_DHCP': is_dhcp, # IP-адрес динамический и присваивается DHCP сервером?
        })

    @pyqtSlot(str)
    def log(self, s):
        """ PyConsole
            @param s: The string
        """
        print(s)