#defining  a class
class S21Ultra:

    #what the class knows
    camera='300mb'
    length=18
    width=19
    ram=15
    memory=300

    #waht the does
    def mobile_spec(self):
        """"class funtion  demo"""
        prompt1='camera capcity'
        prompt3='phone width'

        print(f"{prompt1} : {self.camera}\n length :{self.length}\n {prompt3}{self.width}")

#creating object
device1=S21Ultra()
#here in this code devicel is passed as an argument 
S21Ultra.mobile_spec(device1)

#another way of declaring it 
device1.mobile_spec()



