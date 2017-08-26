# -*- coding: utf-8 -*-

from model.user import User


def test_add_user(app):
    old_user = app.user.get_user_list()
    user = User(firstname="Ivan", lastname="Sidorov")
    app.user.add(user)
    new_user = app.user.get_user_list()
    assert len(old_user) + 1 == len(new_user)
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)