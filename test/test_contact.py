__author__ = 'sergei'

import re
from model.user import User


def test_contact_info_on_home_page(app, db):
    contact_from_home_page = sorted(app.user.get_user_list(),  key=User.id_or_max)
    contact_from_db = sorted(db.get_user_list(),  key=User.id_or_max)
    phones_from_db = list(merge_phones_like_on_home_page(contact_from_db[i]) for i in range(len(contact_from_db)))
    phones_from_home_page = list(contact_from_home_page[i].all_phones_from_page for i in range(len(contact_from_home_page)))
    emails_from_db = list(merge_email_like_on_home_page(contact_from_db[i]) for i in range(len(contact_from_db)))
    emails_from_home_page = list(contact_from_home_page[i].all_email_from_page for i in range(len(contact_from_home_page)))

    assert contact_from_home_page == contact_from_db
    assert phones_from_db == phones_from_home_page
    assert emails_from_db == emails_from_home_page

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