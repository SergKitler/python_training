# -*- coding: utf-8 -*-

from model.user import User
import random
import string


def test_add_user(app):
    old_user = app.user.get_user_list()
    user = User(firstname="Ivan", lastname="Sidorov",
                home=''.join([random.choice(string.digits) for i in range(10)]),
                mobile=''.join([random.choice(string.digits) for i in range(10)]),
                work=''.join([random.choice(string.digits) for i in range(10)]),
                phone2=''.join([random.choice(string.digits) for i in range(10)]))
    app.user.add(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)

#def test_add_user2(app):
#    old_user = app.user.get_user_list()
#    user = User(firstname="Sanya", lastname="Beliy")
#    app.user.add(user)
#    assert len(old_user) + 1 == app.user.count()
#    new_user = app.user.get_user_list()
#    old_user.append(user)
#    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)