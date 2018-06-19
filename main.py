#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import talk_with_user
import krb5_conf
import host_conf
import resolv_conf
import ntp_conf

try:
    import apt
except ImportError:
    os.system("sudo apt update")
    os.system("sudo apt -y install python3-pip")
    os.system("sudo apt install python-apt")
    os.system("sudo pip3 install python-apt")
    import apt

def main(app_conf):
    resolv_conf.update_resolv_conf(app_conf)
    os.system("sudo /etc/init.d/networking restart")
    host_conf.set_hostname(app_conf)
    host_conf.set_hosts(app_conf)
    ntp_conf.time_autosinc(app_conf)
    os.system("sudo /etc/init.d/ntp restart")
    krb5_conf.change_krb5_conf(app_conf)

def update_packages():
    apt_package_list = ['krb5-user', 'samba', 'winbind', 'libpam-krb5', 'libpam-winbind', 'libnss-winbind', 'ntp']
    cache = apt.Cache()
    for apt_package in apt_package_list:
        if not cache[apt_package].is_installed:
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system('sudo apt install {}'.format(' '.join(apt_package_list)))
            break

if __name__ == '__main__':
    update_packages()
    if len(sys.argv) == 1:
        app_conf = talk_with_user.get_params()
        sys.exit(main(app_conf))
    else:
        pass
        # arg_parser = argparse.ArgumentParser(description='Find similar images.')
        # arg_parser.add_argument('-r', '--rar',
        #     nargs='?',
        #     metavar='rar',
        #     dest='rar',
        #     const='fias_delta_dbf',
        #     default='fias_delta_dbf',
        #     help='a rar with *.dbf files')
        # arg_parser.add_argument('-d', '--date',
        #     nargs='?',
        #     metavar='date',
        #     dest='date',
        #     const=None,
        #     default=None,
        #     help='a date')
        # args = arg_parser.parse_args()
        # sys.exit(main(args.date, args.rar))





