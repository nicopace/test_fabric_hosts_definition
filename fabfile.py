from fabric.api import env, run

if not env.hosts:
    env.hosts = ['127.0.0.1', 'localhost']


def mytask():
    run('ls /var/www')
