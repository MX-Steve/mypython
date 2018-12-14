import os
import tarfile
# tar bao

#ya suo
tar = tarfile.open('/tmp/security.tar.gz','w:gz')
os.chdir('/etc')
tar.add('security')
tar.add('hosts')
tar.close()

#jie ya suo
os.mkdir('/tmp/anquan')
os.chdir('/tmp/anquan')
tar = tarfile.open("/tmp/security.tar.gz","r:gz")
#
tar.extractall()
tar.close()