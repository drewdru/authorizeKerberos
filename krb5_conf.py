#! ./env/bin/python
def get_krb5_server_params(app_conf):
    kdc_list = []
    admin_server = ''
    for dns in app_conf['DNS_LIST']:
        server = '{}.{}'.format(dns['host'], app_conf['DOMAIN'])
        kdc_list.append('kdc = {}'.format(server))
        if 'is_admin_server' in dns and dns['is_admin_server']:
            admin_server = server
    return kdc_list, admin_server

def change_krb5_conf(app_conf):
    kdc_list, admin_server = get_krb5_server_params(app_conf)
    with open('./krb5.conf', 'r') as fin:
        with open('/etc/krb5.conf', 'w') as fout:
            fin_data = fin.read()
            if admin_server == '':
                fin_data.replace('admin_server =', '')
            fout.write(fin_data.format(
                app_conf['DOMAIN'].upper(),
                app_conf['DOMAIN'].upper(),
                '\n\t\t'.join(kdc_list),
                admin_server,
                app_conf['DOMAIN'].upper(),
                app_conf['DOMAIN'].upper(),
                app_conf['DOMAIN'].upper()
            ))