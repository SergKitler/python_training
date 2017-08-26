__author__ = 'sergei'

from model.user import User

class UserHelper:
    def __init__(self,app):
        self.app = app

    def add(self, user):
        wd = self.app.wd
        # init new user creation
        wd.find_element_by_link_text("add new").click()
        #fill user form
        self.fill_user_form(user)
        # submit new user creation
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
        self.modify_field_value("email", user.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").click()
        self.modify_field_value("byear", user.byear)

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
        self.user_cache = None

    def delete_all_user(self):
        wd = self.app.wd
        #select all user
        wd.find_element_by_id("MassCB").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

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
        self.user_cache = None

    def edit_first_user_via_edit(self,group):
        wd = self.app.wd
        # start modify first user form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #fill user form
        self.fill_user_form(group)
        #update user edition
        wd.find_element_by_name("update").click()
        self.user_cache = None

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
        self.user_cache = None

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
        self.user_cache = None

    def open_birthday_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/birthdays.php"):
            wd.find_element_by_link_text("next birthdays").click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/"):
            wd.find_element_by_link_text("home").click()

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
                    cells = element.find_elements_by_tag_name("td")[2]
                    firstname = cells.text
                    cells = element.find_elements_by_tag_name("td")[1]
                    lastname = cells.text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    self.user_cache.append(User(firstname=firstname, lastname=lastname, id=id))
        return list(self.user_cache)