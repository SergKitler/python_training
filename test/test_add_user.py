# -*- coding: utf-8 -*-

from model.user import User


def test_test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add(User(firstname="Ivan", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                      email="iii@testinggroup.com", byear="1980"))
    app.session.logout()

