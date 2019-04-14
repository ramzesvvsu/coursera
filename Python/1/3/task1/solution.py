class FileReader:
    def __init__(self, name):
        self.name = name

    def read(self):
        try:
            with open(self.name, "r") as f:
                return(f.read())
        except(OSError, IOError):
            return ""
if __name__ == '__main__':
    reader = FileReader("example.txt")
    print(reader.read())
