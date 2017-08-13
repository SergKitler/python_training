__author__ = 'sergei'

from model.group import Group


def test_edit_group_name(app):
     if app.group.count() == 0:
          app.group.create(Group(name="TestBeforeEditGroup"))
     app.group.edit_first_group(Group(name="TestEditGroup2"))

def test_edit_group_header(app):
     if app.group.count() == 0:
          app.group.create(Group(header="TestBeforeEditGroupHeader"))
     app.group.edit_first_group(Group(header="TestEditGroupHeader"))