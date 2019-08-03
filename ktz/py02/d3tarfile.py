import  tarfile

tar = tarfile.open('/tmp/mytest.tar.gz','w:gz')

tar.add('/etc/hosts')
tar.add('/etc/security')
tar.close()
#
tar = tarfile.open('/tmp/mytest.tar.gz')
tar.extractall(path='/var/tmp')
tar.close()






#
# sys , os , subprocess , getpass , string , shutil , hashlib , functools , time , datetime , random ,