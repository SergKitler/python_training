# -*- coding: utf-8 -*-

from model.user import User


def test_add_user(app):
    app.user.add(User(firstname="Ivan", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                      email="iii@testinggroup.com", byear="1980"))
