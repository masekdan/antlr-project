
class VirtualMachine():
    def __init__(self,file):
        self.file=file
        self.instructions = []
        self.labels = {}
        self.stack = []
        self.memory = {}
        self.IP = 0

        for line in self.file:
            self.instructions.append(line.strip())
    
    def add(self,T):
        if T == "I":
            self.stack[-2] = int(self.stack[-2])+int(self.stack[-1])
        else:
            self.stack[-2] = float(self.stack[-2])+float(self.stack[-1])
        self.stack.pop()

    def sub(self,T):
        if T == "I":
            self.stack[-2] = int(self.stack[-2])-int(self.stack[-1])
        else:
            self.stack[-2] = float(self.stack[-2])-float(self.stack[-1])
        self.stack.pop()

    def mul(self,T):
        if T == "I":
            self.stack[-2] = int(self.stack[-2])*int(self.stack[-1])
        else:
            self.stack[-2] = float(self.stack[-2])*float(self.stack[-1])
        self.stack.pop()

    def div(self,T):
        if T == "I":
            self.stack[-2] = int(self.stack[-2])/int(self.stack[-1])
        else:
            self.stack[-2] = float(self.stack[-2])/float(self.stack[-1])
        self.stack.pop()

    def mod(self):
        self.stack[-2] = int(self.stack[-2])%int(self.stack[-1])
        self.stack.pop()

    def uminus(self,T):
        if T == "I":
            self.stack[-1] = int(self.stack[-2])*(-1)
        else:
            self.stack[-1] = float(self.stack[-2])*(-1)

    def concat(self):
        self.stack[-2] = str(self.stack[-2])+str(self.stack[-1])
        self.stack.pop()

    def andIns(self):
        self.stack[-2] = bool(self.stack[-2]) and bool(self.stack[-1])
        self.stack.pop()
    
    def orIns(self):
        self.stack[-2] = bool(self.stack[-2]) or bool(self.stack[-1])
        self.stack.pop()

    def gt(self,T):
        self.stack[-2] = bool(self.stack[-2] > self.stack[-1])
        self.stack.pop()

    def lt(self,T):
        self.stack[-2] = bool(self.stack[-2] < self.stack[-1])
        self.stack.pop()

    def eq(self,T):
        self.stack[-2] = bool(self.stack[-2] == self.stack[-1])
        self.stack.pop()

    def notIns(self):
        self.stack[-1] = bool(not self.stack[-1])

    def itof(self):
        self.stack[-1]=float(self.stack[-1])

    def pushIns(self,T,x):
        if T == "I":
            self.stack.append(int(x))
        elif T == "F":
            self.stack.append(float(x))
        elif T == "S":
            self.stack.append(x[1:-1])
        elif T == "B":
            if x == "true":
                self.stack.append(bool(True))
            else:
                self.stack.append(bool(False))

    def popIns(self):
        self.stack.pop()

    def loadIns(self,id):
        self.stack.append(self.memory[id])

    def saveIns(self,id):
        self.memory[id] = self.stack[-1]

    def label(self,n):
        pass

    def jmp(self,n):
        self.IP = n

    def fjmp(self,n):
        self.IP = n

    def printIns(self,n):
        pass

    def readIns(self,T):
        pass

    def eval(self):
        for i in range(len(self.instructions)):
            line = self.instructions[i].split()
            instruction = line[0]
            if instruction=="push":
                if line[1]=="S":
                    string = ""
                    for i in (2,len(line)-1):
                        string = string+line[i]
                    self.pushIns(line[1],string)
                else:
                    self.pushIns(line[1],line[2])
            elif instruction=="pop":
                self.popIns()
            elif instruction=="add":
                self.add(line[1])
            elif instruction=="sub":
                self.sub(line[1])
            elif instruction=="mul":
                self.mul(line[1])
            elif instruction=="div":
                self.div(line[1])
            elif instruction=="mod":
                self.mod()
            elif instruction=="uminus":
                self.uminus(line[1])
            elif instruction=="concat":
                self.concat()
            elif instruction=="and":
                self.andIns()
            elif instruction=="or":
                self.orIns()
            elif instruction=="gt":
                self.gt(line[1])
            elif instruction=="lt":
                self.lt(line[1])
            elif instruction=="eq":
                self.eq(line[1])
            elif instruction=="not":
                self.notIns()
            elif instruction=="itof":
                self.itof()
            elif instruction=="load":
                self.loadIns(line[1])
            elif instruction=="save":
                self.saveIns(line[1])
            elif instruction=="label":
                pass
            elif instruction=="jmp":
                self.jmp(line[1])
            elif instruction=="fjmp":
                self.fjmp(line[1])
            elif instruction=="print":
                self.printIns(line[1])
            elif instruction=="read":
                self.readIns(line[1])
            
            self.IP += 1
            i = self.IP 
        
        print(self.stack)