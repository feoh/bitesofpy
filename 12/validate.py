from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here

class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass

def get_secret_token(username):

    maybe_user = [user for user in USERS if user.name == username]

    if not maybe_user:
        raise UserDoesNotExist
    else:
        user = maybe_user[0]

    if user.expired: 
        raise UserAccessExpired
    elif user.role is not ADMIN: 
        raise UserNoPermission
    else:
        return SECRET
