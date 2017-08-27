__author__ = 'sergei'

from model.user import User
from random import randrange


def test_delete_first_user(app):
     if app.user.count() == 0:
          app.user.add(User(firstname="Jeck"))
     old_user = app.user.get_user_list()
     index = randrange(len(old_user))
     app.user.delete_user_by_index(index)
     assert len(old_user) - 1 == app.user.count()
     new_user = app.user.get_user_list()
     old_user[index:index+1] = []
     assert old_user == new_user