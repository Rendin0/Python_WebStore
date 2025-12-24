from User import User

class Consumer(User):
    def __init__(self, login, pwd_hash):
        super().__init__(login, pwd_hash)
    
    