import platform

platform_name = platform.system()
if platform_name == 'SunOS':
    from zfstest.disk_illumos import *
def foo():
    print 'hi'
