class IRCode:
    def __init__(self, key, code):
        self.key = key
        self.code = int(code)

    def get_code(self):
        return self.code

    def get_type(self):
        return self.key

    def to_dict(self):
        return {
            'key': self.key,
            'code': self.code
        }

    @staticmethod
    def from_dict(key, data):
        return IRCode(key, int(data['code']))
