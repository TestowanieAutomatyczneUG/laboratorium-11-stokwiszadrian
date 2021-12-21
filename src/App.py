import os


class App:
    def readcontent(self, path):
        with open(path, 'r') as f:
            return f.read()

    def readline(self, path):
        with open(path, 'r') as f:
            return f.readline()

    def appendfile(self, path, content):
        with open(path, 'a') as f:
            f.write(content)

    def writefile(self, path, content):
        with open(path, "w") as f:
            f.write(content)

    def deletefile(self, path):
        os.remove(path)