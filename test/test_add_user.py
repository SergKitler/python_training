# -*- coding: utf-8 -*-

from model.user import User

def test_add_user(app, json_users):
    user = json_users
    old_user = app.user.get_user_list()
    app.user.add(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)