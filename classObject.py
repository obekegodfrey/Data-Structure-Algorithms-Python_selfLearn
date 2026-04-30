class student:
    rn=123
    name="abc"
    branch="cse"
    def read(self):
        print("reading ")
        rno=345
        print(rno)

abc=student()
print("rno", student.rn) 
print("name", abc.name)
print("branch",abc.branch)  
abc.read()   

 