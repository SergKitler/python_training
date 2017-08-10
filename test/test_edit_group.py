__author__ = 'sergei'

from model.group import Group


def test_edit_group(app):
     app.session.login(username="admin", password="secret")
     app.group.edit_first_group(Group(name="TestEditGroup", header="TestEditGroupHeader", footer="TestEditGroupFooter"))
     app.session.logout()