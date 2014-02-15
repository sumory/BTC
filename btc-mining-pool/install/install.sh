#apt-get
sudo apt-get install `cat apt-get-install.list | grep -v '#'`

#pip install
sudo pip install `cat pip-install.list | grep -v '#'`
