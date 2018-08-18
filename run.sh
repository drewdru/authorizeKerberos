./check_sudo.sh
if [ $? -eq 0 ]; then
    ./install_python.sh
    if [ $? -eq 0 ]; then
        RUN="./main.py $@" 
        sudo $RUN
    fi
else
    exit -1
fi

