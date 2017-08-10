__author__ = 'sergei'

class UserHelper:
    def __init__(self,app):
        self.app = app

    def add(self, group):
        wd = self.app.wd
        # init new user creation
        wd.find_element_by_link_text("add new").click()
        # fill user form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(group.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group.company)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(group.byear)
        # submit new user creation
        wd.find_element_by_name("submit").click()

    def delete_first_user(self):
        wd = self.app.wd
        #select first user
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
