class Contact:
    def __init__(self, firstname, nickname, mobile):
        self.firstname = firstname
        self.nickname = nickname
        self.mobile = mobile
        self.id = id

    def __repr__(self):
        return f'{self.id}, {self.firstname}'
