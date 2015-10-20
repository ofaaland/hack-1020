from subprocess import Popen
from subprocess import PIPE


def create(pool_name, pool_type, vdev_list):
    """
    sadflkj

    :param pool_name: The name of the pool
    :type pool_name: ``str``
    :param pool_type: The type of vdev config
    :type pool_name: ``str``
    :param vdev_list: The vdevs needed to create the pool
    :type vdev_list: ``list`` of strings
    """
    cmd = ['sudo', 'zpool', 'create', pool_name]
    if len(pool_type):
        cmd += [pool_type]
    cmd += vdev_list

    try:
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        proc.stdin.close()
        while proc.returncode is None:
            proc.poll()
    except:
        pass


def destroy(pool_name):
    cmd = ['sudo', 'zpool', 'destroy', pool_name]

    try:
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        proc.stdin.close()
        while proc.returncode is None:
            proc.poll()
    except:
        pass
