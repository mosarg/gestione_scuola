import gdata.apps.multidomain.client
import hashlib




def passwd(username, password):
    client = gdata.apps.multidomain.client.MultiDomainProvisioningClient(domain="linussio.it")
    client.ssl = True
    client.ClientLogin(email="administrator@linussio.it", password="Samback@999", source='apps')

    password = hashlib.sha1(password).hexdigest()
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
    return "password changed"



