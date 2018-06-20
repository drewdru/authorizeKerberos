#! ./env/bin/python
import file_helper

def set_hosts(app_conf):
    file_helper.add_string_to_file('127.0.1.1 {}.{} {}'.format(
        app_conf['HOSTNAME'], 
        app_conf['DOMAIN'], 
        app_conf['HOSTNAME']), '/etc/hosts')

def set_hostname(app_conf):
    with open('/etc/hostname', 'w') as hostname_file:
        hostname_file.write(app_conf['HOSTNAME'])

