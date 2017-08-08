# -*- coding: utf-8 -*-

import pytest
from user import Add_user
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_user(app):
    app.login(username="admin", password="secret")
    app.add_new_user(Add_user(firstname="Ivan", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                          email="iii@testinggroup.com", byear="1980"))
    app.logout()

