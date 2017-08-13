__author__ = 'sergei'

class UserHelper:
    def __init__(self,app):
        self.app = app

    def add(self, group):
        wd = self.app.wd
        # init new user creation
        wd.find_element_by_link_text("add new").click()
        #fill user form
        self.fill_user_form(group)
        # submit new user creation
        wd.find_element_by_name("submit").click()

    def fill_user_form(self, group):
        wd = self.app.wd
        self.modify_field_value("firstname",group.firstname)
        self.modify_field_value("middlename",group.middlename)
        self.modify_field_value("lastname",group.lastname)
        self.modify_field_value("nickname",group.nickname)
        self.modify_field_value("title",group.title)
        self.modify_field_value("company",group.company)
        self.modify_field_value("email", group.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").click()
        self.modify_field_value("byear", group.byear)

    def modify_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_user(self):
        wd = self.app.wd
        #select first user
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def delete_all_user(self):
        wd = self.app.wd
        #select all user
        wd.find_element_by_id("MassCB").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def edit_first_user_via_deteils(self,group):
        wd = self.app.wd
        #select first user
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        #start modify user form
        wd.find_element_by_name("modifiy").click()
        #fill user form
        self.fill_user_form(group)
        #update user edition
        wd.find_element_by_name("update").click()

    def edit_first_user_via_edit(self,group):
        wd = self.app.wd
        # start modify first user form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #fill user form
        self.fill_user_form(group)
        #update user edition
        wd.find_element_by_name("update").click()

    def edit_first_user_via_birthday_deteils(self,group):
        wd = self.app.wd
        #open birthday page
        self.open_birthday_page()
        #select first user
        wd.find_element_by_xpath("//table[@id='birthdays']/tbody/tr[2]/td[7]/a/img").click()
        #start modify user form
        wd.find_element_by_name("modifiy").click()
        #fill user form
        self.fill_user_form(group)
        #update user edition
        wd.find_element_by_name("update").click()

    def edit_first_user_via_birthday_edit(self,group):
        wd = self.app.wd
        # open birthday page
        self.open_birthday_page()
        # start modify first user form
        wd.find_element_by_xpath("//table[@id='birthdays']/tbody/tr[2]/td[8]/a/img").click()
        #fill user form
        self.fill_user_form(group)
        #update user edition
        wd.find_element_by_name("update").click()

    def open_birthday_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("next birthdays").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))