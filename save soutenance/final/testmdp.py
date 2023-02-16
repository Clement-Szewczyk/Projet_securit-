import bcrypt


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


hash = hashpassword('testmdp')
print(verifpassword('testmdp', hash))
