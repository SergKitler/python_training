__author__ = 'sergei'

from model.group import Group


def test_edit_group_name(app):
     if app.group.count() == 0:
          app.group.create(Group(name="TestBeforeEditGroup"))
     old_groups = app.group.get_group_list()
     group = Group(name="TestEditGroup2")
     group.id = old_groups[0].id
     app.group.edit_first_group(group)
     assert len(old_groups) == app.group.count()
     new_groups = app.group.get_group_list()
     old_groups[0] = group
     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#          app.group.create(Group(header="TestBeforeEditGroupHeader"))
#     app.group.edit_first_group(Group(header="TestEditGroupHeader"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)