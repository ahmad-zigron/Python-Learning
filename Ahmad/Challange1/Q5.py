class IOstring():


    def getStr(self):
        self.s = raw_input()

    def printStr(self):
        print self.s

strObj = IOstring()
strObj.getStr()
strObj.printStr()
