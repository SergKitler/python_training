__author__ = 'sergei'

from model.group import Group
from random import randrange


def test_edit_group_name(app, db):
     if len(db.get_group_list()) == 0:
          app.group.create(Group(name="TestBeforeEditGroup"))
     old_groups = db.get_group_list()
     index = randrange(len(old_groups))
     group = Group(name="TestEditGroup2", header="TestHeader2", footer="TestFooter2")
     group.id = old_groups[index].id
     app.group.edit_group_by_index(index, group)
     assert len(old_groups) == app.group.count()
     new_groups = db.get_group_list()
     old_groups[index] = group
     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
