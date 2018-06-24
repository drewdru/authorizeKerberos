import os
import krb5_conf
import host_conf
import resolv_conf
import ntp_conf

def update(app_conf):
    resolv_conf.update_resolv_conf(app_conf)
    host_conf.set_hostname(app_conf)
    host_conf.set_hosts(app_conf)
    ntp_conf.time_autosinc(app_conf)
    os.system('sudo /etc/init.d/ntp restart')
    krb5_conf.change_krb5_conf(app_conf)
