__author__ = 'sergei'

from model.group import Group
from model.user import User
import random


def test_del_user_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.user.add(User(firstname="Jeck", lastname="Antonio"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="TestGroup"))
    old_group = orm.get_group_list()
    group = random.choice(old_group)
    old_users_in_group = orm.get_contacts_in_group(group)
    if len(old_users_in_group) == 0:
        old_users = orm.get_contact_list()
        user_in_group = User(firstname="Jeck2", lastname="Antonio")
        app.user.add(user_in_group)
        new_users = orm.get_contact_list()
        old_id = list(old_users[i].id for i in range(len(old_users)))
        id = list(new_users[i].id for i in range(len(new_users)) if new_users[i].id not in old_id )
        print(id)
        app.user.add_user_by_id_to_group(id[0],group.id)
        user_in_group.id = id[0]
        old_users_in_group.append(user_in_group)
    user = random.choice(old_users_in_group)
    app.user.del_user_by_id_from_group(user.id, group.id)
    new_users_in_group = orm.get_contacts_in_group(group)
    old_users_in_group.remove(user)
    assert old_users_in_group == new_users_in_group
