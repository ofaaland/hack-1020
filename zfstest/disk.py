import platform

platform_name = platform.system()
if platform_name == 'SunOS':
    from zfstest.disk_illumos import *
elif platform_name == 'Linux':
    from zfstest.disk_linux import *

def foo():
    print 'hi'
