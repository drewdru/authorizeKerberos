#! ./env/bin/python
import file_helper

def get_dhclient_data(dhclient_conf_path):
    ip_list = []
    old_line = ''
    with open(dhclient_conf_path, 'r') as dhclient_file:
        is_have_DNS = False
        for line in dhclient_file:
            if 'prepend domain-name-servers' in line and '#' not in line:
                is_have_DNS = True
                old_line = line
                line.replace(';', '')
                line.replace('prepend domain-name-servers', '')
                ip_list = line.split(',')
        return ip_list, old_line, is_have_DNS

def add_DNS_to_DHCP_config(app_conf):
    dhclient_conf_path = '/etc/dhcp/dhclient.conf'
    ip_list, old_line, is_have_DNS = get_dhclient_data(dhclient_conf_path)
    for dns in app_conf['DNS_LIST']:
        if dns['ip'] not in ip_list:
            ip_list.append(dns['ip'])
    ip_list_str = ', '.join(ip_list)
    prepend_dns = 'prepend domain-name-servers {};'.format(ip_list_str)
    if is_have_DNS:
        file_helper.replace_file_line(dhclient_conf_path, old_line, prepend_dns)
    if not is_have_DNS:
        with open(dhclient_conf_path, 'a') as dhclient_file:
            dhclient_file.write('\n{}'.format(prepend_dns)) 

def update_resolv_conf(app_conf):
    resolv_conf_path = '/etc/resolvconf/resolv.conf.d/head' if app_conf['IS_AUTO_RESOLV'] else '/etc/resolv.conf'
    if not app_conf['IS_AUTO_RESOLV']:
        file_helper.add_string_to_file('domain {}'.format(app_conf['DOMAIN']), resolv_conf_path)
        file_helper.add_string_to_file('search {}'.format(app_conf['DOMAIN']), resolv_conf_path)
    for dns in app_conf['DNS_LIST']:
        file_helper.add_string_to_file('nameserver {}'.format(dns['ip']), resolv_conf_path)
    if app_conf['IS_DHCP']:
        file_helper.add_string_to_file('supersede domain-name "{}"'.format(app_conf['DOMAIN']), 
            '/etc/dhcp/dhclient.conf')
        add_DNS_to_DHCP_config(app_conf)