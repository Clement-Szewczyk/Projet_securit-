'''import bcrypt
from common.models import student


def hashpassword(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password, salt)
    return hashed

# verification si mdp donnée est le même que celui de la bdd qui a été hashé


def verifpassword(password, hashed):
    password = password.encode('utf-8')

    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False


student.objects.create(email="toto@gmail.com", password=hashpassword("toto"))
mdp = student.objects.get(email="toto@gmail.com").password
print(mdp)
print(verifpassword("toto", mdp))
'''
