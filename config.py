from easyos import easyos
import random
import string

def return_or_make_secret_key(secret_key_file):
    # If we don't have a secret access key for signing sessions, make one
    try:
        with open(secret_key_file, "r") as f:
            return f.read()
    except IOError:
        print("Creating secret_key file")
        l = random.randint(25, 50)
        _rand = "".join(random.choice(string.printable) for i in range(l))
        with open(secret_key_file, "w+") as f:
            f.write(_rand)
            return f.read()


class BaseConfig:
    LISTEN_HOST = '127.0.0.1'
    LISTEN_PORT = 5000

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = return_or_make_secret_key(easyos["tmp_dir"] + "ffi4wd_development_csrf_key")