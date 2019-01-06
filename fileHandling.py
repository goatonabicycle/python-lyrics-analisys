

class fileHandling(object):
    def writeToFile(self, fileName, content):
        f = open(fileName, "w+")
        f.write(content)
        f.close()
        return "Success! I think."
