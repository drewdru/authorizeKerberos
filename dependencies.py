#! ./env/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import file_helper
from packages_conf import APT_PACKAGES

def install_sudo():
    user = os.popen('whoami').read()
    os.system('su -c "apt-get update"')
    os.system('su -c "apt-get -y upgrade"')
    os.system('su -c "apt-get -y dist-upgrade"')
    os.system('su -c "apt-get -y install sudo"')
    os.system('su -c "usermod -aG sudo {}"'.format(user))
    file_helper.add_string_to_file('{} ALL=(ALL) ALL'.format(user.rstrip()), '/etc/sudoers')

def install_apt_packages():
    os.system('sudo apt-get update')
    os.system('sudo apt-get -y upgrade')
    os.system('sudo apt-get -y dist-upgrade')
    if 'apt-utils' in APT_PACKAGES:
        os.system('sudo apt-get install -y --no-install-recommends apt-utils')
    if 'krb5-user' in APT_PACKAGES:
        # os.system('export DEBIAN_FRONTEND=teletype')
        # os.environ['DEBIAN_FRONTEND'] = 'noninteractive'
        os.system('yes "\n" | sudo apt-get -y --assume-yes install krb5-user')
    print('sudo apt-get -y install {}'.format(' '.join(APT_PACKAGES)))
    os.system('sudo apt-get -y --assume-yes install {}'.format(' '.join(APT_PACKAGES)))

if os.system('sudo apt-get -v') != 0:
    install_sudo()

def update_packages():
    for apt_package in APT_PACKAGES:
        is_install = os.system('dpkg -l {} | grep "ii  {}"'.format(apt_package, apt_package))
        if is_install != 0:
            print('{} does not install !!!!!!!!!!!!!!!!!!!!'.format(apt_package))
            if os.system('sudo apt-get -v') != 0:
                install_sudo()
            install_apt_packages()
            break
    try:
        with open('/etc/default/locale', "r+") as file:
            for line in file:
                if 'LANG=en_US.UTF-8' in line:
                    break
                if 'LANGUAGE=en_US.UTF-8' in line:
                    break
            else:
                # os.system('sudo echo "en_US.UTF-8 UTF-8" > /etc/locale.gen')
                os.system('sudo locale-gen --purge en_US.UTF-8')
                file.write('LC_ALL=en_US.UTF-8\nLANG=en_US.UTF-8\nLANGUAGE=en_US.UTF-8')
    except FileNotFoundError:
        os.system('sudo locale-gen --purge en_US.UTF-8')
        os.system('sudo echo -e "LC_ALL=en_US.UTF-8\nLANG=en_US.UTF-8\nLANGUAGE=en_US.UTF-8" > /etc/default/locale')

    os.system('sudo echo "en_US UTF-8" > /etc/locale.gen')
    os.environ['LC_ALL'] = 'en_US.UTF-8'
    os.environ['LANG'] = 'en_US.UTF-8'
    os.environ['LANGUAGE'] = 'en_US.UTF-8'
    os.system('sudo locale-gen en_US.UTF-8')
    os.system('sudo update-locale LANG=en_US')


