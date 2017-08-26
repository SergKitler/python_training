__author__ = 'sergei'

from model.user import User

def test_edit_user_via_details(app):
    if app.user.count() == 0:
        app.user.add(User(firstname="Jeck", lastname="Antonio"))
    old_user = app.user.get_user_list()
    user = User(firstname="Mikhael", lastname="Maximilianno")
    user.id = old_user[0].id
    app.user.edit_first_user_via_deteils(user)
    new_user = app.user.get_user_list()
    assert len(old_user)  == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)

def test_edit_user_via_edit(app):
    if app.user.count() == 0:
        app.user.add(User(lastname="Smirnov"))
    old_user = app.user.get_user_list()
    user = User(firstname="Semen", lastname="Ivanov")
    user.id = old_user[0].id
    app.user.edit_first_user_via_edit(user)
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)

def test_edit_user_via_birthday_details(app):
    if app.user.count() == 0:
        app.user.add(User(nickname="TestBefoModifyUser"))
    old_user = app.user.get_user_list()
    user = User(firstname="Anton", lastname="Banderos", nickname="TestEditUser")
    user.id = old_user[0].id
    app.user.edit_first_user_via_birthday_deteils(user)
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)

def test_edit_user_via_birthday_edit(app):
    if app.user.count() == 0:
        app.user.add(User(firstname="Jeck2"))
    old_user = app.user.get_user_list()
    user = User(firstname="Samuil", lastname="Ibragimovich", byear="1976")
    user.id = old_user[0].id
    app.user.edit_first_user_via_birthday_edit(user)
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)
