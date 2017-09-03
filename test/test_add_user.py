# -*- coding: utf-8 -*-

from model.user import User
import random
import string

Fname = ["Ivan", "Semen", "Serg", "Konstantin", "Nikolas", "Mosses"]
Lname = ["Brown", "Kaddi", "Bethoven", "Radzinsky", "Runny", "Kazbek"]
Address = ["Tomsk", "Los Angeles", "New-York", "Moscow", "Bangladesh"]
domain = ["mail.ru", "gmail.com", "hotmail.ru", "my.ru"]

def test_add_user(app):
    old_user = app.user.get_user_list()
    user = User(firstname=random.choice(Fname),
                lastname=random.choice(Lname),
                address=random.choice(Address),
                email="@".join([
                    ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(12))]),
                        random.choice(domain)]),
                email2="@".join([
                    ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(12))]),
                    random.choice(domain)]),
                email3="@".join([
                    ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(12))]),
                    random.choice(domain)]),
                home=''.join([random.choice(string.digits) for i in range(10)]),
                mobile=''.join([random.choice(string.digits) for i in range(10)]),
                work=''.join([random.choice(string.digits) for i in range(10)]),
                phone2=''.join([random.choice(string.digits) for i in range(10)]))
    app.user.add(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)

#def test_add_user2(app):
#    old_user = app.user.get_user_list()
#    user = User(firstname="Sanya", lastname="Beliy")
#    app.user.add(user)
#    assert len(old_user) + 1 == app.user.count()
#    new_user = app.user.get_user_list()
#    old_user.append(user)
#    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)