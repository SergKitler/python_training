__author__ = 'sergei'

import re
from random import randrange


def test_contact_info_on_home_page(app):
    index = randrange(app.user.count())
    contact_from_home_page = app.user.get_user_list()[index]
    contact_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_page == merge_email_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter (lambda x: x !="",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [user.home, user.mobile, user.work, user.phone2]))))

def merge_email_like_on_home_page(user):
    return "\n".join(filter (lambda x: x !="",
                             filter(lambda x: x is not None,
                                    [user.email, user.email2, user.email3])))