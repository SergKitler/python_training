# -*- coding: utf-8 -*-

from model.user import User


def test_add_user(app):
    old_user = app.user.get_user_list()
    app.user.add(User(firstname="Ivan", lastname="Sidorov"))
    new_user = app.user.get_user_list()
    assert len(old_user) + 1 == len(new_user)