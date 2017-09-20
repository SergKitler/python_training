# -*- coding: utf-8 -*-

from model.user import User

def test_add_user(app, db, json_users, check_ui):
    user = json_users
    old_user = db.get_user_list()
    app.user.add(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = db.get_user_list()
    old_user.append(user)
    assert old_user == new_user
    if check_ui:
        def clean(user):
            return User(id=user.id, firstname=user.firstname.strip(), lastname=user.lastname.strip())
        assert sorted(map(clean, new_user), key=User.id_or_max) == sorted(app.user.get_user_list(),
                                                                             key=User.id_or_max)