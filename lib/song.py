
class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album

    def save(self):
        # Your save logic here
        pass

    @classmethod
    def create_table(cls):
        # Your create table logic here
        pass

    @classmethod
    def create(cls, name, album):
        # Your create logic here
        pass
