from fabric.api import hosts, run

@hosts()
def passwd(username, password):
        print "Change samba4 password"
        command = "samba-tool user setpassword"
        command += " "+username+" --newpassword "+password
        return run(command)

