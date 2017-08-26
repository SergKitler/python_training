__author__ = 'sergei'

from model.user import User


def test_delete_all_users(app):
     if app.user.count() == 0:
          app.user.add(User(firstname="Jeck"))
     app.user.delete_all_user()
     new_user = app.user.get_user_list()
     assert len(new_user) == 0