__author__ = 'sergei'

class Group:

    def __init__(self,name,header,footer):
        self.name = name
        self.header = header
        self.footer = footer

class Group_for_user:

    def __init__(self,firstname,middlename,lastname,nickname,title,company,email,byear):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.email = email
        self.byear = byear