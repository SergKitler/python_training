# -*- coding: utf-8 -*-

from model.user import User
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    return  "+" +''.join([random.choice(string.digits) for i in range(maxlen)])

def random_email(maxlen,maxdomainlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    #domain = string.ascii_letters + string.digits + string.punctuation + " " * 10 + "." * 10
    symbols = string.ascii_letters + string.digits + " " * 10
    domain = string.ascii_letters + string.digits +  " " * 10 + "." * 10
    return "@".join(["".join([random.choice(symbols) for i in range(random.randrange(maxlen))]),
                     "".join([random.choice(domain) for i in range(random.randrange(maxdomainlen))])])

testdata = [User(firstname="", lastname="", address="")] +[
     User(firstname=random_string("Firstname",10),
           lastname=random_string("Lastname",20),
           address=random_string("Address",20),
           home=random_phone(10),
           mobile=random_phone(10),
           work=random_phone(10),
           phone2=random_phone(10),
           email=random_email(12,12),
           email2=random_email(12,12),
           email3=random_email(12,12),
           )
     for i in range(2)
]

@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_user = app.user.get_user_list()
    app.user.add(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)