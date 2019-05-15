

class fileHandling(object):    
    def writeToFile(self, fileName, content):
        try:
            f = open(fileName, "w+")
            f.write(content)
            f.close()
            return "Success! I think."
        except:
            return "Failed. Dismally."
