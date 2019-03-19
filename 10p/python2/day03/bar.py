import foo
print(foo.hi)

import sys
print(sys.path)

# import shutil
# shutil.copy("foo.py",'/usr/local/lib/python3.6/site-packages/')

# site-packages
# export PYTHONPATH=the path where py is
from mypkg import hi
hi.say()

from pkg import hi
hi.say()

from . import foo
print(foo.hi)