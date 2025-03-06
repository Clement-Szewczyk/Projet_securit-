import hashlib

liste = ['a', 'b']

print(hash('toto'))
print(hash('toto'))
print(hash('toyo'))

if hash('toto') == hash('toto'):
    print('ok')
else:
    print('no')
