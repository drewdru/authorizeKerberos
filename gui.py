#! ./env/bin/python
import os

try:
    import PyQt5
except ImportError:
    os.system('sudo apt-get update')
    os.system('sudo apt-get -y install python3-pip')
    os.system('./env/bin/pip3 install PyQt5')
    import PyQt5

def update_packages():
    os.system("export QT_X11_NO_MITSHM=1")
    apt_package_list = ['mesa-utils', 'build-essential', 'mesa-common-dev', 'libfontconfig1', 'libglu1-mesa-dev', 'python3-opengl', 'python3-pyqt5', 'python3-pyqt5.qtopengl', 'python3-pyqt5.qtquick']
    for apt_package in apt_package_list:
        is_install = os.system('dpkg -l {} | grep "ii  {}"'.format(apt_package, apt_package))
        if is_install != 0:
            os.system('sudo add-apt-repository ppa:ubuntu-x-swat/updates')
            os.system('sudo apt-get update')
            os.system('sudo apt-get -y upgrade')
            os.system('sudo apt-get -y install {}'.format(' '.join(apt_package_list)))
            break

def main_gui():
    pass