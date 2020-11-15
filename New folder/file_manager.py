class FileMenager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self, file_name):
        dane = file_name.read()
        print(dane)

    def update_file(self, text_data):
        with open(self.file_name, "a") as file:
            file.write(text_data)


