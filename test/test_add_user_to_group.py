__author__ = 'sergei'

from model.group import Group
from model.user import User
import random

def test_add_user_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.user.add(User(firstname="Jeck", lastname="Antonio"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="TestGroup"))
    old_group = orm.get_group_list()
    group = random.choice(old_group)
    old_users_out_of_group = orm.get_contacts_not_in_group(group)
    old_users_in_group = orm.get_contacts_in_group(group)
    if len(old_users_out_of_group) == 0:
        old_users_out_of_group.append(app.user.add(User(firstname="Jeck", lastname="Antonio")))
    user = random.choice(old_users_out_of_group)
    app.user.add_user_by_id_to_group(user.id, group.id)
    new_users_in_group = orm.get_contacts_in_group(group)
    old_users_in_group.append(user)
    assert old_users_in_group == new_users_in_group