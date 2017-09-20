__author__ = 'sergei'

from model.user import User
import random


def test_delete_user(app, db, check_ui):
     if len(db.get_user_list()) == 0:
          app.user.add(User(firstname="Jeck"))
     old_user = db.get_user_list()
     user = random.choice(old_user)
     app.user.delete_user_by_id(user.id)
     assert len(old_user) - 1 == app.user.count()
     new_user = db.get_user_list()
     old_user.remove(user)
     assert old_user == new_user
     if check_ui:
          assert sorted(new_user, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)
