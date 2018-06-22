# PKG_OK=$(dpkg-query -W --showformat='${Status}\n' python3.6|grep "install ok installed")
# echo Checking for somelib: $PKG_OK
# if [ "" == "$PKG_OK" ]; then
python3.6 -V
if [ $? -eq 0 ]; then
    echo "python3.6 is installed"
else
    sudo apt-get update && apt-get -y upgrade
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev
    sudo apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
    sudo apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev
    sudo apt-get -y install wget tar virtualenv
    wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
    tar xvf Python-3.6.5.tgz
    cd Python-3.6.5
    ./configure --enable-optimizations --with-ensurepip=install
    make
    make altinstall
    cd ..
    rm -rf ./Python-3.6.5*
    rm -rf ./env
fi

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' virtualenv|grep "install ok installed")
echo Checking for virtualenv: $PKG_OK
if [ "" == "$PKG_OK" ]; then
    sudo apt-get update && apt-get -y upgrade
    sudo apt-get -y install virtualenv
fi

if [ ! -d "./env" ]; then
    virtualenv env --python python3.6
fi
