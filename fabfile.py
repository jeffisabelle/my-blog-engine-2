from fabric.api import run, env, cd


CODE_DIR = '/srv/flask/muhammetcan2'
env.user = 'root'
env.hosts = ['muhammetcan']
env.use_ssh_config = True
env.forward_agent = True


def install_dependencies():
    run('pip install -r requirements.txt')


def release():
    with cd(CODE_DIR):
        run('git fetch')
        run('git pull -u origin master')
        install_dependencies()
