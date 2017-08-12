__author__ = 'sergei'

from model.group import Group


def test_edit_group_name(app):
     app.session.login(username="admin", password="secret")
     app.group.edit_first_group(Group(name="TestEditGroup2"))
     app.session.logout()

def test_edit_group_header(app):
     app.session.login(username="admin", password="secret")
     app.group.edit_first_group(Group(header="TestEditGroupHeader"))
     app.session.logout()