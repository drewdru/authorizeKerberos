#!./env/bin/python
# -*- coding: utf-8 -*-
import os
try:
    import npyscreen
except ImportError:
    os.system('sudo ./env/bin/pip install --upgrade pip')
    os.system('./env/bin/pip install npyscreen')
    import npyscreen
import config
import change_configs


class MyTestApp(npyscreen.NPSAppManaged):        
    def onStart(self, args={}):
        self.IS_HAVENT_ADMIN_SERVER = True            
        self.addForm("MAIN", MainForm, name='Настройки авторизации Kerberos')
        self.addForm("ADD_DNS", Add_DnsForm)

class Add_DnsForm(npyscreen.FormWithMenus):
    def create(self):
        self.host = self.add(npyscreen.TitleText, name="DNS сервер домена (dc):")
        self.ip = self.add(npyscreen.TitleText, name="IP адрес DNS сервера (192.168.0.1):")
        if self.parentApp.IS_HAVENT_ADMIN_SERVER:
            self.is_admin_server = self.add(npyscreen.TitleSelectOne, max_height=4, value = [0,], name="Является первичным DNS сервером домена?",
                values = ["да", "нет"], scroll_exit=True)
        self.is_add_dns = self.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Добавить ещё один DNS сервер?",
                values = ["да", "нет"], scroll_exit=True)
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

    def afterEditing(self):
        config.app_conf['DNS_LIST'].append({
            'host': self.host.value,
            'ip': self.ip.value,
            'is_admin_server': True if self.is_admin_server.value[0] == 0 else False,
        })
        if self.is_admin_server.value[0] == 0:
            self.parentApp.IS_HAVENT_ADMIN_SERVER = False
        if self.is_add_dns.value[0] == 0:
            self.parentApp.setNextForm('ADD_DNS')
        else:
            self.parentApp.setNextForm(None)

class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.domain = self.add(npyscreen.TitleText, name="Домен для входа (example.com):")
        self.is_add_dns = self.add(npyscreen.TitleSelectOne, max_height=4, value = [0,], name="Добавить DNS сервер?",
                values = ["да", "нет"], scroll_exit=True)
        self.hostname = self.add(npyscreen.TitleText, name="HOSTNAME данного компьютера (smbsrv01):")
        self.time_server = self.add(npyscreen.TitleText, name="Сервер для автоматической синхронизации времени (dc.domain.com):")
        self.is_auto_resolv = self.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Поддерживает ли сервер автоматическое создание файла resolv.conf?",
                values = ["да", "нет"], scroll_exit=True)
        self.is_dhcp = self.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="IP-адрес динамический и присваивается DHCP сервером?",
                values = ["да", "нет"], scroll_exit=True)
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application

    def exit_application(self):
        if self.is_add_dns.value == 0:
            self.parentApp.setNextForm('ADD_DNS')
            self.parentApp.switchFormNow()
        else:
            self.parentApp.setNextForm(None)
            self.editing = False
            self.parentApp.switchFormNow()

    def afterEditing(self):
        if self.domain.value == '' or self.hostname.value == '' or self.time_server.value == '':
            return
        if self.domain.value != '':
            config.app_conf['DOMAIN'] = self.domain.value
        if self.hostname.value != '':
            config.app_conf['HOSTNAME'] = self.hostname.value
        if self.time_server.value != '':
            config.app_conf['TIME_SERVER'] = self.time_server.value
        config.app_conf['IS_AUTO_RESOLV'] = True if self.is_auto_resolv.value[0] == 0 else False
        config.app_conf['IS_DHCP'] = True if self.is_dhcp.value[0] == 0 else False
        config.app_conf['DNS_LIST'] = []
        if self.is_add_dns.value[0] == 0:
            self.parentApp.setNextForm('ADD_DNS')
            self.parentApp.switchFormNow()
        else:
            self.parentApp.setNextForm(None)

def main():
    TA = MyTestApp()
    TA.run()
    change_configs.update(config.app_conf)

if __name__ == '__main__':
    main()
