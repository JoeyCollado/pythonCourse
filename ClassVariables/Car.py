class Car:
    
    def __init__(self,make,model,year,color): #special method, in other programming language its called constructor
                                              #self represents the object were creating
                                              #parameters are arguments that a constructor needs in order to create the object
        #attributes
      self.make = make
      self.model = model
      self.year = year
      self.color = color  
    #methods
    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
