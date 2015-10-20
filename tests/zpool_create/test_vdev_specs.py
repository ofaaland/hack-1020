from zfstest import disk
from zfstest import zpool


def test_001():
    pool_types = ['', 'mirror', 'raidz', 'raidz1', 'raidz2']
    disk_list = disk.find_free_disks()
    for pool_type in pool_types:
        create_pool_tests('testpool')
    return True
