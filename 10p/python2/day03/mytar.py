import tarfile
# import shutil
import os

# tar = tarfile.open('/tmp/security.tar.gz','w:gz')
# tar.add('/tmp/passwd')
# tar.add('/etc/security')
# tar.close()

# tar = tarfile.open('/tmp/security.tar.gz','r:gz')
# tar.extractall()
# tar.close()

# tar = tarfile.open('bar.tar.gz','w:gz')
# tar.add('bar.py')
# tar.close()

# os.remove('bar.py')

tar = tarfile.open('bar.tar.gz','r:gz')
tar.extractall()
tar.close()