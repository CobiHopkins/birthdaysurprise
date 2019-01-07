"""Download and install database essentials and Python3 modules necessary for bot functionality and compatability with Discord."""

import os, sys, time

print('Installing MySql Server...')
os.system('sudo apt-get install mysql-server')
os.system('systemctl enable mysql')
os.system('systemctl start mysql')
time.sleep(1)

print('Obtaining necessary Python3 modules...')
os.system('pip3 install mysql-connector')
os.system('pip3 install discord.py')
