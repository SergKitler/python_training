__author__ = 'sergei'

from model.user import User

def test_delete_first_user(app):
     if app.user.count() == 0:
          app.user.add(User(firstname="Jeck"))
     old_user = app.user.get_user_list()
     app.user.delete_first_user()
     new_user = app.user.get_user_list()
     assert len(old_user) - 1 == len(new_user)
     old_user[0:1] = []
     assert old_user == new_user