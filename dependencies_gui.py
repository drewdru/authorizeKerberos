#! ./env/bin/python
# -*- coding: utf-8 -*-
import os
APT_PACKAGE_LIST = ['mesa-utils', 'build-essential', 'mesa-common-dev', 'libfontconfig1', 'libglu1-mesa-dev', 'python3-pyqt5']

def install_apt_packages():
    os.environ['QT_X11_NO_MITSHM'] = '1'
    os.system('sudo apt-get update')
    os.system('sudo apt-get -y upgrade')
    os.system('sudo apt-get -y dist-upgrade')
    os.system('sudo apt-get -y --assume-yes install {}'.format(' '.join(APT_PACKAGE_LIST)))

try:
    import PyQt5
except ImportError:
    os.system('sudo ./env/bin/pip install --upgrade pip')
    os.system('./env/bin/pip install PyQt5')
    import PyQt5

def update_packages():
    # TODO: pip packages
    for apt_package in APT_PACKAGE_LIST:
        is_install = os.system('dpkg -l {} | grep "ii  {}"'.format(apt_package, apt_package))
        if is_install != 0:
            install_apt_packages()
            break
