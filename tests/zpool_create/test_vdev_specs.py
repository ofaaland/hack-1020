from zfstest import disk
from zfstest import zpool

def _create_pool_tests(pool_name, vdev_spec):
    zpool.create(pool_name, vdev_spec)
    return False


def test_001():
    vdev_specs = ['', 'mirror', 'raidz', 'raidz1', 'raidz2']
    disk_list = disk.find_free_disks()

    #zpool.create('testpool', '', ['c1t1d0', 'c1t2d0'])
    zpool.create('testpool', 'mirror', ['c1t1d0', 'c1t2d0'])

    #for pool_type in pool_types:
    #    _create_pool_tests('testpool', pool_type)
