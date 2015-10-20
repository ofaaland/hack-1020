from zfstest import disk
from zfstest import zpool

def _create_pool_tests(pool_name, pool_type, vdev_spec):
    # vdev_spec = vdev_spec[:2]
    zpool.create(pool_name, pool_type, vdev_spec)
    zpool.destroy(pool_name)


def test_whole_disks():
    pool_types = ['', 'mirror', 'raidz', 'raidz1', 'raidz2']
    disk_list = disk.find_free_disks()

    for pool_type in pool_types:
        _create_pool_tests('testpool', pool_type, disk_list)
