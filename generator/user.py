from model.user import User
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of user","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o in "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    return  "+" +''.join([random.choice(string.digits) for i in range(maxlen)])

def random_email(maxlen,maxdomainlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    domain = string.ascii_letters + string.digits + string.punctuation + " " * 10 + "." * 10
    return "@".join(["".join([random.choice(symbols) for i in range(random.randrange(maxlen))]),
                     "".join([random.choice(domain) for i in range(random.randrange(maxdomainlen))])])

testdata = [User(firstname="", lastname="", address="")] +[
     User(firstname=random_string("Firstname",10),
           lastname=random_string("Lastname",20),
           address=random_string("Address",20),
           home=random_phone(10),
           mobile=random_phone(10),
           work=random_phone(10),
           phone2=random_phone(10),
           email=random_email(12,12),
           email2=random_email(12,12),
           email3=random_email(12,12),
           )
     for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w")as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))