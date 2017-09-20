__author__ = 'sergei'

from model.user import User
import random

def test_edit_user_via_details(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.add(User(firstname="Jeck", lastname="Antonio"))
    old_user = db.get_user_list()
    user = random.choice(old_user)
    user_change = User(firstname="Mikhael", lastname="Maximilianno")
    app.user.edit_user_by_id_via_deteils(user.id, user_change)
    assert len(old_user)  == app.user.count()
    new_user = db.get_user_list()
    old_user[old_user.index(user)] = user_change
    assert old_user == new_user
    if check_ui:
        def clean(user):
            return User(id=user.id, firstname=user.firstname.strip(), lastname=user.lastname.strip())
        assert sorted(map(clean, new_user), key=User.id_or_max) == sorted(app.user.get_user_list(),
                                                                             key=User.id_or_max)


def test_edit_user_via_edit(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.add(User(firstname="Alex", lastname="Smirnov"))
    old_user = db.get_user_list()
    user = random.choice(old_user)
    user_change = User(firstname="Semen", lastname="Ivanov")
    app.user.edit_user_by_id_via_edit(user.id, user_change)
    assert len(old_user) == app.user.count()
    new_user = db.get_user_list()
    old_user[old_user.index(user)] = user_change
    assert old_user == new_user
    if check_ui:
        def clean(user):
            return User(id=user.id, firstname=user.firstname.strip(), lastname=user.lastname.strip())

        assert sorted(map(clean, new_user), key=User.id_or_max) == sorted(app.user.get_user_list(),
                                                                          key=User.id_or_max)


