__author__ = 'sergei'

from model.user import User
import re


class UserHelper:
    def __init__(self,app):
        self.app = app

    def add(self, user):
        wd = self.app.wd
        # init new user creation
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(user)
        wd.find_element_by_name("submit").click()
        self.user_cache = None

    def fill_user_form(self, user):
        wd = self.app.wd
        self.modify_field_value("firstname", user.firstname)
        self.modify_field_value("middlename", user.middlename)
        self.modify_field_value("lastname", user.lastname)
        self.modify_field_value("nickname", user.nickname)
        self.modify_field_value("title", user.title)
        self.modify_field_value("company", user.company)
        self.modify_field_value("address", user.address)
        self.modify_field_value("home", user.home)
        self.modify_field_value("work", user.work)
        self.modify_field_value("mobile", user.mobile)
        self.modify_field_value("phone2", user.phone2)
        self.modify_field_value("email", user.email)
        self.modify_field_value("email2", user.email2)
        self.modify_field_value("email3", user.email3)

    def modify_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        #select first user
        wd.find_elements_by_name("selected[]")[index].click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def delete_user_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_user_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def select_user_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("table#maintable input[id='%s']" % id).click()

    def delete_all_user(self):
        wd = self.app.wd
        #select all user
        wd.find_element_by_id("MassCB").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def edit_first_user_via_deteils(self, group):
        self.edit_user_by_index_via_deteils(0, group)

    def edit_user_by_index_via_deteils(self, index, user):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        wd.find_element_by_name("modifiy").click()
        self.fill_user_form(user)
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def edit_user_by_id_via_deteils(self, id, user):
        wd = self.app.wd
        self.open_user_view_by_id(id)
        wd.find_element_by_name("modifiy").click()
        self.fill_user_form(user)
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        element = wd.find_elements_by_css_selector("table#maintable tr[name=entry]")[index]
        cell = element.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_user_view_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("table#maintable a[href='view.php?id=%s']" % id).click()


    def edit_first_user_via_edit(self, group):
        self.edit_user_by_index_via_edit(0, group)

    def edit_user_by_index_via_edit(self, index, group):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        self.fill_user_form(group)
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        element = wd.find_elements_by_css_selector("table#maintable tr[name=entry]")[index]
        cell = element.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def edit_user_by_id_via_edit(self, id, group):
        wd = self.app.wd
        self.open_user_to_edit_by_id(id)
        self.fill_user_form(group)
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def open_user_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("table#maintable a[href='edit.php?id=%s']" % id).click()

    def edit_first_user_via_birthday_deteils(self,group):
        wd = self.app.wd
        #open birthday page
        self.open_birthday_page()
        #select first user
        wd.find_element_by_xpath("//table[@id='birthdays']/tbody/tr[2]/td[7]/a/img").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_user_form(group)
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def edit_first_user_via_birthday_edit(self,group):
        wd = self.app.wd
        # open birthday page
        self.open_birthday_page()
        # start modify first user form
        wd.find_element_by_xpath("//table[@id='birthdays']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_user_form(group)
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def open_birthday_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/birthdays.php"):
            wd.find_element_by_link_text("next birthdays").click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/"):
            wd.find_element_by_link_text("home").click()
        #wd.find_element_by_css_selector('form#right option[value=""]').click()

    def count(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_xpath("//table[@id='maintable']//a[.='Last name']")) > 0):
            wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.user_cache = []
            for element in wd.find_elements_by_css_selector("table#maintable tr[name=entry]"):
                    cells = element.find_elements_by_tag_name("td")
                    lastname = cells[1].text
                    firstname = cells[2].text
                    address = cells[3].text
                    all_email = cells[4].text
                    all_phones = cells[5].text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    self.user_cache.append(User(firstname=firstname, lastname=lastname, id=id,
                                                address=address, all_email_from_page=all_email,
                                                all_phones_from_page=all_phones))
        return list(self.user_cache)

    def get_user_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return User(firstname=firstname, lastname=lastname, id=id, address=address,
                    email=email, email2=email2, email3=email3,
                    home=homephone, mobile=mobilephone,
                    work=workphone, phone2=phone2)


    def get_user_from_view_page(self,index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return User(home=homephone, mobile=mobilephone,  work=workphone, phone2=phone2)

    def add_user_by_id_to_group(self,id,group_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_user_by_id(id)
        wd.find_element_by_css_selector("div#content select[name='to_group']>option[value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()

    def del_user_by_id_from_group(self,id,group_id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("form#right option[value='%s']" % group_id).click()
        self.select_user_by_id(id)
        wd.find_element_by_name("remove").click()