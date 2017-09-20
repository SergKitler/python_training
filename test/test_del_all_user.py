__author__ = 'sergei'

from model.user import User


def test_delete_all_users(app, db):
     if len(db.get_user_list()) == 0:
          app.user.add(User(firstname="Jeck"))
     app.user.delete_all_user()
     new_user = db.get_user_list()
     assert len(new_user) == 0