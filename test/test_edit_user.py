__author__ = 'sergei'

from model.user import User


def test_edit_user_via_details(app):
    app.user.edit_first_user_via_deteils(User(firstname="Mikhael"))

def test_edit_user_via_edit(app):
    app.user.edit_first_user_via_edit(User(lastname="Ivanov"))

def test_edit_user_via_birthday_details(app):
    app.user.edit_first_user_via_birthday_deteils(User(nickname="TestEditUser"))

def test_edit_user_via_birthday_edit(app):
    app.user.edit_first_user_via_birthday_edit(User(firstname="Samuil", middlename="Ibragimovich", byear="1976"))
