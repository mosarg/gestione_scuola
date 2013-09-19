from django.contrib.auth.models import User


def passwd(username, password):
    try:
       print "Change django password"
       user=User.objects.get(username=username)
       user.set_password(password)
       user.save()
       return "password changed"
    except Exception as e:
       return "error "+e.args

