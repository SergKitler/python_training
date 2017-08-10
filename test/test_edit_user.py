__author__ = 'sergei'

from model.user import User


def test_test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.edit_first_user_via_deteils(User(firstname="Mikhael", middlename="Ivanovich", lastname="Sidorov", nickname="TestUser", title="test", company="TestingGroup",
                                  email="iii@testinggroup.com", byear="1980"))
    app.session.logout()