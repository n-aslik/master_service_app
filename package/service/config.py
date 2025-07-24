from configparser import ConfigParser

class Keys:
    def __init__(self):
        with open("package\service\private_key.pem", "rb") as priv:
            self.private_key = priv.read()
        with open("package\service\public_key.pem","rb") as pub:
            self.public_key = pub.read()