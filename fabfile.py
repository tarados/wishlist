from fabric.api import run, cd, env, local

CONF = {
    'site': {
        'hosts': ['dmitryzvada@dev.avallon.im'],
        'host': 'dmitryzvada@dev.avallon.im',
        'project': 'wishlist',
        'root': '/opt/sites/wishlist/',
        'uwsgi_conf': '/etc/uwsgi_py3/available/wishlist.ini',
    }
}


def pull():
    with cd('%(root)ssrc/' % env):
        run('git pull')


def pip_install():
    run('%(root)senv/bin/pip install -r %(root)ssrc/requirements.txt' % env)


def collect_static():
    run(django_command('collectstatic --noinput -v0') % env)


def reload_uwsgi():
    run('sudo touch --no-dereference %(uwsgi_conf)s' % env)


def push():
    local('git push')


def syncdb():
    run(django_command('migrate') % env)


def python(command):
    return '%(root)senv/bin/python' + ' ' + command


def django_command(command):
    return python('%(root)ssrc/manage.py') + ' ' + command


def init_env(name):
    for k, v in CONF[name].items():
        setattr(env, k, v)


init_env('site')


def update():
    init_env('site')
    push()
    pull()
    pip_install()
    collect_static()
    syncdb()
    reload_uwsgi()


def update_fast():
    init_env('site')
    push()
    pull()
    collect_static()
    reload_uwsgi()


def only_reload():
    init_env('site')
    reload_uwsgi()
