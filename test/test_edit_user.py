__author__ = 'sergei'

from model.user import User

def test_edit_user_via_details(app):
    old_user = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.add(User(firstname="Jeck"))
    app.user.edit_first_user_via_deteils(User(firstname="Mikhael"))
    new_user = app.user.get_user_list()
    assert len(old_user)  == len(new_user)

def test_edit_user_via_edit(app):
    old_user = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.add(User(lastname="Smirnov"))
    app.user.edit_first_user_via_edit(User(lastname="Ivanov"))
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)

def test_edit_user_via_birthday_details(app):
    old_user = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.add(User(nickname="TestBefoModifyUser"))
    app.user.edit_first_user_via_birthday_deteils(User(nickname="TestEditUser"))
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)

def test_edit_user_via_birthday_edit(app):
    old_user = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.add(User(firstname="Jeck2"))
    app.user.edit_first_user_via_birthday_edit(User(firstname="Samuil", middlename="Ibragimovich", byear="1976"))
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
