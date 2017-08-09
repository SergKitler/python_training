# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.user import Add_user


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add(Add_user(firstname="Ivan", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                          email="iii@testinggroup.com", byear="1980"))
    app.session.logout()

