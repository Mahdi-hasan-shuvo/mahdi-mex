import os,time
os.system('clear')
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
    print(' \n\033[1;37m Congratulations! Your Device Support This Tools');time.sleep(2)
    import mahdii
else:
   import shuvo
