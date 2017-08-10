__author__ = 'sergei'

def test_delete_first_group(app):
     app.session.login(username="admin", password="secret")
     app.user.delete_all_user()
     app.session.logout()