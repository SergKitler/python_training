__author__ = 'sergei'

from model.user import User


def test_edit_user_via_details(app):
    app.session.login(username="admin", password="secret")
    app.user.edit_first_user_via_deteils(User(firstname="Mikhael", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                                  email="iii@testinggroup.com", byear="1980"))
    app.session.logout()

def test_edit_user_via_edit(app):
    app.session.login(username="admin", password="secret")
    app.user.edit_first_user_via_edit(User(firstname="Daniil", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                                  email="iii@testinggroup.com", byear="1982"))
    app.session.logout()

def test_edit_user_via_birthday_details(app):
    app.session.login(username="admin", password="secret")
    app.user.edit_first_user_via_birthday_deteils(User(firstname="Mikhael", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                                  email="iii@testinggroup.com", byear="1980"))
    app.session.logout()

def test_edit_user_via_birthday_edit(app):
    app.session.login(username="admin", password="secret")
    app.user.edit_first_user_via_birthday_edit(User(firstname="Mikhael", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                                  email="iii@testinggroup.com", byear="1980"))
    app.session.logout()