#!/home/apps/.virtualenvs/gestione_scuola/bin/python
import os
import csv
import sys
from optparse import OptionParser
import gdata.apps.multidomain.client
import hashlib

sys.path.append("/home/apps/webapps/gestione_scuola")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestione_scuola.settings.local")

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from backend.models import Backend
from account.models import Account
import django.db.utils

usage="usage: %prog <command> <username> --name <Name> --surname <Surname> --password <Password> --email <Email>"

parser = OptionParser(usage)
parser.add_option('-n', '--name', dest='name', metavar='NAME', help="User full name")
parser.add_option('-s', '--surname', dest='surname', metavar='SURNAME',help="User lastname")
parser.add_option('-p', '--password', dest='password', metavar='PASSWORD', help="User password")
parser.add_option('-e', '--email', dest='email', metavar='EMAIL',help="User email")
parser.add_option('-f', '--file', dest='file',metavar='FILE',help="Bulf email file")

(options, args) = parser.parse_args()

command=args[0]
username=args[1]

if command=='add':
 try:
    user = User.objects.create_user(username, options.email, options.password)
    user.last_name=options.surname
    user.first_name=options.name
    #default group
    group=Group.objects.get(name='frontend')
    user.groups.add(group)
    print user.id
 except django.db.utils.IntegrityError:
   print "duplicate entry"
 except:
   print "error" 

elif command=='delete':
    try:
        user=User.objects.get(username=username)
        user.delete()
        print "user delete successfull"
    except:
        print "user not found"
elif command=='check':
    try:
        user=User.objects.get(username=username)
        print "user present"
    except:
         print "user not found"   
elif command=="setpassword":
    try:
       user=User.objects.get(username=username)
       user.set_password(options.password)
       user.save()
        
    except Exception as e:
       print "error"
elif command=="bulkpassword":
    with open(options.file,'rb') as f:
      reader=csv.DictReader(f)
      for row in reader:
        print "Change django password for "+row['username']+" "+row['password']
        try:
          user=User.objects.get(username=row['username'])
          user.set_password(row['password'])
          user.save()
        except Exception as e:
          print "error"

elif command=="test":
    djangoBackend=Backend.objects.get(kind='samba4')
    account=Account.objects.filter(backendId=djangoBackend.backendId).get(username=username)
    account.changeBackendPassword()
elif command=="setgpassword":
    client = gdata.apps.multidomain.client.MultiDomainProvisioningClient(domain="linussio.it")
    client.ssl = True
    client.ClientLogin(email="administrator@linussio.it", password="Samback@999", source='apps')
    password = hashlib.sha1(options.password).hexdigest()
    mail=username+"@linussio.it"
    try:
      user = client.RetrieveUser(mail)
    except:
      print '[WARNING] Account %s not found' % mail
    user.password = password
    user.hash_function="SHA-1"
    try:
      client.UpdateUser(mail, user)
      print '[NOTICE] Updated password for %s' % mail
    except:
      print '[ERROR] Could not update password for %s ' % mail                      

else:
    print(command+" not found\n")




