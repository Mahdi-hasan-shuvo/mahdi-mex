import os,time
os.system('clear')
#os.system('xdg-open https://facebook.com/ma4D1')
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
    print(' \n\033[1;37m Congratulations! Your Device Support This Tools');time.sleep(2)
    import mahdii
else:
   import shuvo
