__author__ = 'sergei'

from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
     if len(db.get_group_list()) == 0:
          app.group.create(Group(name="TestBeforeEditGroup"))
     old_groups = db.get_group_list()
     group = random.choice(old_groups)
     group_change = Group(name="TestEditGroup2", header="TestHeader2", footer="TestFooter2")
     app.group.edit_group_by_id(group.id, group_change)
     assert len(old_groups) == app.group.count()
     new_groups = db.get_group_list()
     old_groups[old_groups.index(group)] = group_change
     assert old_groups == new_groups
     if check_ui:
          def clean(group):
               return Group(id=group.id, name=group.name.strip())
          assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
