from fabric.api import env, run, sudo, get, put, task

env.user = "alexandro"

env.hosts = [
#	'104.131.177.202',
	'45.55.166.170',
]
@task
def nro_procesos():
	run("ps -aux | wc -l")

@task
def update():
	print("Actualizando la lista de paquetes")
	sudo("apt-get update")

@task
def upgrade():
	print("Actualizando servidor")
	sudo("apt-get update")
	sudo("apt-get upgrade")

@task
def lamp():
	sudo("apt-get install -y apache2")
	sudo("apt-get install -y mysql-server")
	sudo("systemctl restart mysql.service")
	sudo("apt-get -y install php5 php-pear php5-mysql")
	sudo("apt-get -y install phpmyadmin")
