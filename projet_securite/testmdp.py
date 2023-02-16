import bcrypt


'''def hashpw(pwd):
    salt = bcrypt.gensalt(rounds=14)
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), salt)
    return hashed


# Generate an encrypted password -or get the one stored in database -
mdp_u = "toto"
mdp_user_crypted = hashpw(mdp_u)

# Ask for a password :
mdp_input = "toto"

# check with the 'checkpw' function
# param_1 = utf8 encoded input
# param_2 = crypted password stored
test = mdp_input.encode('utf-8')
print(test)
result = bcrypt.checkpw(test, mdp_user_crypted)
print(mdp_u, mdp_input, result)

# check with the 'checkpw' function
# param_1 = utf8 encoded input
# param_2 = crypted password stored
mdp_input = "tata"
result = bcrypt.checkpw(mdp_input.encode('utf-8'), mdp_user_crypted)
print(mdp_u, mdp_input, result)'''


password = "super secret password"
password = password.encode('utf-8')
# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# Check that an unhashed password matches one that has previously been
# hashed

if bcrypt.checkpw(password, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")
