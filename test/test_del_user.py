__author__ = 'sergei'

from model.user import User

def test_delete_first_group(app):
     if app.user.count() == 0:
          app.user.add(User(firstname="Jeck"))
     app.user.delete_first_user()