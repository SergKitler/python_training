__author__ = 'sergei'
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.user import User
from pymysql.converters import encoders, decoders, convert_mysql_timestamp

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups',
                       column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups',
                     column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name,
                         header=group.header, footer=group.footer)
        return list(map(convert,groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return User(id=contact.id, firstname=contact.firstname,
                        lastname=contact.lastname)
        return list(map(convert,contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(list(select(g for g in ORMFixture.ORMGroup)))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None)))

    @db_session
    def get_contacts_in_group(self,group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups)))

