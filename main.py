#!./env/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import dependencies
import talk_with_user
import config
import main_gui
import main_ci
import change_configs

class StoreDictKeyPair(argparse.Action):
     def __call__(self, parser, namespace, values, option_string=None):
         my_arr = []
         for kd in values.split(","):
            my_dict = {}
            for kv in kd.split("+"):
                k,v = kv.split("=")
                my_dict[k] = v
            my_arr.append(my_dict)
         setattr(namespace, self.dest, my_arr)


if __name__ == '__main__':
    dependencies.update_packages()
    arg_parser = argparse.ArgumentParser(description='Set up Kerberos authorize')
    arg_parser.add_argument('-g', '--gui',
        action='store_true',
        help='Запустить с графическим интерфейсом')
    arg_parser.add_argument('--ci',
        action='store_true',
        help='Запустить с консольным интерфейсом')
    arg_parser.add_argument('--console',
        action='store_true',
        help='Запустить в консольном режиме')
    arg_parser.add_argument('-d', '--domain',
        nargs='?',
        help='Домен для входа\tПример: domain.com')
    arg_parser.add_argument('--hostname',
        nargs='?',
        help='HOSTNAME данного компьютера\tПример: smbsrv01')
    arg_parser.add_argument('-t', '--time_server',
        nargs='?',
        help='Сервер для автоматической синхронизации\tПример: dc.domain.com')
    arg_parser.add_argument('--auto_resolv',
        action='store_true',
        help='Поддерживает ли сервер автоматическое создание файла resolv.conf?')
    arg_parser.add_argument('--dhcp',
        action='store_true',
        help='IP-адрес динамический и присваивается DHCP сервером?')
    arg_parser.add_argument("--dns_list", 
        action=StoreDictKeyPair, 
        help="Список DNS домена (host=dc+ip=192.168.0.1+is_admin_server=True,host=dc2+ip=192.168.0.2)")
    args = arg_parser.parse_args()
    if len(sys.argv) >= 1:
        if args.domain is not None:
            config.app_conf['DOMAIN'] = args.domain
        if args.hostname is not None:
            config.app_conf['HOSTNAME'] = args.hostname
        if args.time_server is not None:
            config.app_conf['TIME_SERVER'] = args.time_server
        if args.dns_list is not None:
            config.app_conf['DNS_LIST'] = args.dns_list
        config.app_conf['IS_AUTO_RESOLV'] = args.auto_resolv
        config.app_conf['IS_DHCP'] = args.dhcp
        # print(config.app_conf)
        if args.gui:
            main_gui.main()
        elif args.console:
            if 'DOMAIN' not in config.app_conf \
                    or 'HOSTNAME' not in config.app_conf \
                    or 'TIME_SERVER' not in config.app_conf \
                    or 'DNS_LIST' not in config.app_conf \
                    or 'IS_AUTO_RESOLV' not in config.app_conf \
                    or 'IS_DHCP' not in config.app_conf:
                print('Введены не все параметры!')
                app_conf = talk_with_user.get_params(config.app_conf)
            sys.exit(change_configs.update(app_conf))
        else:
            main_ci.main()
    else:
        main_ci.main()
        # app_conf = talk_with_user.get_params()
        # sys.exit(change_configs.update(app_conf))





