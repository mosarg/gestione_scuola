from fabric.api import hosts, run


@hosts()
def passwd(username, password):
        command = "samba-tool user setpassword"
        command += " "+username+" --newpassword "+password
        return run(command)

