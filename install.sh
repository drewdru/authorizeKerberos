su -c "apt-get update && apt-get -y upgrade"
su -c "apt-get install -y make build-essential libssl-dev zlib1g-dev"
su -c "apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm"
su -c "apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev"
su -c "apt-get -y install wget tar virtualenv"

python3.6 -V
if [ $? -eq 0 ]; then
    echo 'python3.6 already installed'
else
    wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
    tar xvf Python-3.6.5.tgz
    cd Python-3.6.5
    ./configure --enable-optimizations --with-ensurepip=install
    make
    make altinstall
    cd ..
    rm -rf ./Python-3.6.5*
fi
rm -rf env
virtualenv env --python python3.6




