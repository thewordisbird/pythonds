import pdb

class LogicGate:

    def __init__(self, name):
        self.name = name
        self.output = None

    def getLabel(self):
        return self.name
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
class BinaryGate(LogicGate):

    def __init__(self, name, pinA=None, pinB=None):
        LogicGate.__init__(self, name)

        self.pinA = pinA
        self.pinB = pinB

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class NandGate(AndGate):   
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NorGate(OrGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 0 and b == 1:
            return 1
        elif a == 1 and b == 0:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self, name):
        LogicGate.__init__(self, name)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() +"-->"))   
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):
    
    def __init__(self, name):
        UnaryGate.__init__(self, name)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fromGate, toGate):
        self.fromGate = fromGate
        self. toGate = toGate

        toGate.setNextPin(self)
       
    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate




def half_adder():
        # create gate objects
        #pdb.set_trace()
        g1 = XorGate('G1')
        g2 = AndGate('G2')

        # Prompt user for A and B inputs
        #signal_a = int(input('Enter input A: '))
        #signal_b = int(input('Enter input B: '))

        # Set gate input pins
        #g1.pinA = g2.PinA = signal_a
        #g1.pinB = g2.PinB = signal_b

        # Get gate outputs
        sum = g1.getOutput()
        carry = g2.getOutput()

        return sum, carry

def full_adder():
    g1 = XorGate('G1')
    g2 = AndGate('G2')
    g3 = XorGate('G3')
    g4 = AndGate('G4')
    g5 = OrGate('G5')

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g5)
    


if __name__ == '__main__':
    
    print(half_adder())