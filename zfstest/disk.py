import platform
from zfstest.config import *

platform_name = platform.system()
if platform_name == 'SunOS':
    from zfstest.disk_illumos import *
elif platform_name == 'Linux':
    from zfstest.disk_linux import *

def foo():
    print 'hi'

# the config file is loaded and queried here
# until we have a session initialization method
# somewhere.  Then we can load the config there
# and just fetch the relevant value here
def disk_list():
    cfg = load_config()
    return cfg['test_disks']
