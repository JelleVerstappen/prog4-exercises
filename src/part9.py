class Book:
    def __init__(self, title):
        self.title = title
        self.content = f"Title: {self.title}\n"

    def add_chapter(self, chapter):
        self.content += f'# {chapter}\n'

    def add_line(self, lines):
        self.content += f'{lines}\n'

    def write(self, filename):
        file = open(filename, "wt")
        file.write(self.content)
        