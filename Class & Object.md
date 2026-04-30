class can be defined by data and functions

class members can be accessed by object.
class can be referenced by object

class student has data(stdno, name, branch) and functions(read() and write()). to accesss student class we need to create an object.

in python, a class is a block of statement.

### syntax for class ###
class classname:
    data
    functions

class student:
    rno = 123
    name = "abc"
    branch = "cse"
    def read(self):
        print("read")
    def write(self):
        print("write")   

* variables defined inside in a class not inside function is a instance variables   
* variables defined 

### syntax for object ###
object_name = class_name()   
s1 = student()  
s2 = student() 

s1.rno
s1.name
s1.branch

