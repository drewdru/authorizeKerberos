import file_helper
def time_autosinc(app_conf):
    file_helper.add_string_to_file('server {}'.format(
        app_conf['TIME_SERVER']), '/etc/ntp.conf')
