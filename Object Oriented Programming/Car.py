class Car:
    
    #instance variable are declared inside the constructor
    #clsss variable they are declared within a class but outside of constructor, you can set default values for all the instances of this class
    
    wheels = 2 #class variable
    
    def __init__(self,make,model,year,color): #special method, in other programming language its called constructor
                                              #self represents the object were creating
                                              #parameters are arguments that a constructor needs in order to create the object
        #attributes
      self.make = make                        #instance variables and each object can have their own unique values assinged to each variables
      self.model = model                      #instance variables and each object can have their own unique values assinged to each variables
      self.year = year                        #instance variables and each object can have their own unique values assinged to each variables
      self.color = color                      #instance variables and each object can have their own unique values assinged to each variables
    #methods
    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

  
