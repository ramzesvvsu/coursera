from tempfile import gettempdir
from os.path import join
import tempfile
class File:
    def __init__(self, filename):
        self.filename = filename

    def write(self, row):
        with open(self.filename, 'a') as f:
            f.write(row)

    def __add__(self, other):
        tfile = tempfile.NamedTemporaryFile(delete=False)
        with open(tfile.name, 'a+') as f:
            f.write(self.readfile())
            f.write(other.readfile())
        #return self.__str__() +
        return File(tfile.name)

    def __str__(self):
        return self.filename

    def __iter__(self):
        yield from open(self.filename)

    def readfile(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def __next__(self):
        with open(self.filename, 'r') as f:
            for fileline in f.readlines():
                yield fileline
        raise StopIteration

if __name__ == '__main__':
    obj = File('C:\\1\\1.txt')
    obj.write('line\n')
    first = File('C:\\1\\2.txt')
    second = File('C:\\1\\3.txt')

    new_obj = first + second
    for line in File('C:\\1\\1.txt'):
      print(line)
    print(obj)