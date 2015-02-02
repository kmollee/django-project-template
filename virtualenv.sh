# install pip if it doesn't exist yet
# YUM_CMD=$(which yum)
# APT_GET_CMD=$(which apt-get)
# OTHER_CMD=$(which <other installer>

# if [[ ! -z $YUM_CMD ]]; then
#     yum install $YUM_PACKAGE_NAME
# elif [[ ! -z $APT_GET_CMD ]]; then
#     apt-get $DEB_PACKAGE_NAME
# elif [[ ! -z $OTHER_CMD ]]; then
#     $OTHER_CMD <proper arguments>
# else
#     echo "error can't install package $PACKAGE"
#     exit 1;
# fi

# since python3.4 already build-in pip, no need to install again
echo "pip3 install virtualenv"
sudo pip3 install virtualenv

echo "create virtualenv"
virtualenv --python=python3.4 ./env


# activate virtual env
echo "activate virtualenv"
source ./env/bin/activate

# install dev requirements package
echo "install dev require packages"
./install_dev.sh

echo "finish install"
