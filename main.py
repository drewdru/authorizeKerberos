#!./env/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import dependencies
import talk_with_user
import krb5_conf
import host_conf
import resolv_conf
import ntp_conf

def main(app_conf):
    resolv_conf.update_resolv_conf(app_conf)
    if os.system('sudo /etc/init.d/network-manager restart') != 0:
        os.system('sudo /etc/init.d/networking restart')
    host_conf.set_hostname(app_conf)
    host_conf.set_hosts(app_conf)
    ntp_conf.time_autosinc(app_conf)
    os.system('sudo /etc/init.d/ntp restart')
    krb5_conf.change_krb5_conf(app_conf)

if __name__ == '__main__':
    # test = os.popen('whoami | id | grep sudo -c').read()
    # print(type(test))
    dependencies.update_packages()
    if len(sys.argv) == 1:
        app_conf = talk_with_user.get_params()
        print(app_conf)
        sys.exit(main(app_conf))
    else:
        arg_parser = argparse.ArgumentParser(description='Set up Kerberos authorize')
        # arg_parser.add_argument('--gui', action='store_const', const=42)
        arg_parser.add_argument('-g', '--gui',
            action='store_true',
            help='Запустить с графическим интерфейсом')
        arg_parser.add_argument('-d', '--domain',
            nargs=1,
            help='Домен для входа\tПример: domain.com')
        arg_parser.add_argument('--hostname',
            nargs=1,
            help='HOSTNAME данного компьютера\tПример: smbsrv01')
        arg_parser.add_argument('-t', '--time_server',
            nargs=1,
            help='Сервер для автоматической синхронизации\tПример: dc.domain.com')
        arg_parser.add_argument('--auto_resolv',
            action='store_true',
            help='Поддерживает ли сервер автоматическое создание файла resolv.conf?')
        arg_parser.add_argument('--dhcp',
            action='store_true',
            help='IP-адрес динамический и присваивается DHCP сервером?')
        args = arg_parser.parse_args()
        print(args)
        if args.gui:
            # main_gui()
            print('run with GUI')
        else: 
            print('no GUI')
        # sys.exit(main(args.date, args.rar))





