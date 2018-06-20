#! ./env/bin/python
import os
import sys
import file_helper
from packages_conf import APT_PACKAGES

def install_sudo():
    user = os.popen('whoami').read()
    os.system('su -c "apt-get -y install sudo"')
    os.system('usermod -aG sudo {}'.format(user))
    file_helper.add_string_to_file('{} ALL=(ALL) ALL'.format(user), '/etc/sudoers')
    file_helper.replace_file_line('/etc/sudoers', old_line, prepend_dns)

def install_apt_packages():
    os.system('sudo apt-get update')
    os.system('sudo apt-get -y upgrade')
    os.system('sudo apt-get -y dist-upgrade')
    if 'krb5-user' in APT_PACKAGES:
        os.system('\n | sudo apt-get -y install krb5-user')
    os.system('sudo apt-get -y install {}'.format(' '.join(APT_PACKAGES)))
    
if os.system('sudo apt-get -v') != 0:
    install_sudo()

def update_packages():
    for apt_package in APT_PACKAGES:
        is_install = os.system('dpkg -l {} | grep "ii  {}"'.format(apt_package, apt_package))
        if is_install != 0:
            if apt_package == 'sudo':
                install_sudo()
            install_apt_packages()
            break
    
    with open('/etc/default/locale', "r+") as file:
        for line in file:
            if 'LANG=en_US.UTF-8' in line:
                break
            if 'LANGUAGE=en_US.UTF-8' in line:
                break
        else:
            os.system('locale-gen --purge en_US.UTF-8')
            file.write('LC_ALL=en_US.UTF-8\nLANG=en_US.UTF-8\nLANGUAGE=en_US.UTF-8')

    with open('/etc/default/locale', "r+") as file:
        for line in file:
            if 'allow-hotplug eth0' in line:
                break
            if 'iface eth0 inet dhcp' in line:
                break
        else:
            file.write('\nallow-hotplug eth0\niface eth0 inet dhcp')
