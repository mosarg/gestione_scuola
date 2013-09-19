from fabric.api import hosts, run


@hosts()
def passwd(username, password):
        print "Change moodle password"
        command = "moosh --moodle-path /var/www/moodle "
        command +='user-mod --password '+password+" "+username
        return run(command)
