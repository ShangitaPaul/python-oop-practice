"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # SerialGenerator class allows you to create a serial number generator that starts from a specified number (start) and provides methods to generate the next serial number and reset the generator to its initial state. The generate method increments the serial number by 1 each time it is called, and the reset method sets the serial number back to the starting value.

    #The init method is the constructor of SerialGenerator class to initialize the new instance of the generator class with a starting value "start" that is set to 0 by default.
    #Self is the instance of the class that is being initialized.
    def __init__(self, start=0):
        #Start is stored in the self.start attribute, with self.next being set to the same value.
        self.start = self.next = start
    #The __repr__ method is implemented to provide a string representation of the SerialGenerator object. It returns a formatted string that includes the values of start and next attributes. This representation is helpful when printing the object or using it in the interactive console.
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"
    #The generate method returns the current value of the next attribute and increments it by 1.
    #The generate method is responsible for generating the next serial number in the sequence. It increments the self.next attribute by 1 and returns the previous value (self.next - 1). Each time generate is called, it returns the next number in the sequence.
    def generate(self):
        self.next += 1
        return self.next - 1
    #The reset method resets the generator to the original starting value and sets self.next attribute back to the initial value specified by self.start.
    def reset(self):
        self.next = self.start


    

