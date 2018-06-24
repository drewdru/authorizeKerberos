ROOT_USER=root
USERNAME=$(whoami)
dpkg -l sudo | grep "ii  sudo" -c
if [ $? -eq 0 ]; then
    echo "sudo не установлен. Введите пароль администратора для начала установки"
    su -c "apt-get update"
    su -c "apt-get -y upgrade"
    su -c "apt-get -y dist-upgrade"
    su -c "apt-get -y install sudo"
    su -c "usermod -aG sudo $USERNAME"
    su -c "echo '$USERNAME ALL=(ALL) ALL' >> /etc/sudoers"
fi
IS_CAN_USE_SUDO=$(whoami | id | grep sudo -c)
if [ $IS_CAN_USE_SUDO -eq 0 ]; then
    IS_IN_SUDO_GROUP=$(cat /etc/group |grep sudo |grep $(whoami) -c)
    if [ $IS_IN_SUDO_GROUP -eq 0 ]; then
        echo "$USERNAME не имеет права sudo"
        exit 1
    else
        exit 0
    fi
elif [ $IS_CAN_USE_SUDO -eq 1 ]; then
    exit 0
else
    exit $?
fi