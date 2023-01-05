class employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empCount +=1
    def displayCount(self):
        print("total employee{0}".format(employee.empCount))
    def displayEmployee(self):
        print("name:", self.name, ", salary: ",self.salary)
#emp1=employee("jasmine",90000)
##print("total employee", employee.empCount)
##emp2=employee("Appu",50000)
##emp1.displayEmployee()
##emp2.displayEmployee()
##print("total employee{0}".format(employee.empCount))
##emp3=employee("kishore",80000)
##emp3.displayCount()
##emp2.displayCount()
##emp1.displayCount()
##print("total employee {0}" .format(employee.empCount))


####emp1.displayEmployee()
####emp1.salary=17000
####emp1.experience=3
####emp1.displayEmployee()
####emp1.name='manoj'
####emp1.displayEmployee()
####print(emp1.experience)
#####del emp1.salary
####emp1.displayEmployee()

emp1=employee("jasmine",9999)
emp1.displayEmployee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1, 'salary'))
setattr(emp1, 'salary',7000)    
print("modified salary",getattr(emp1, 'salary'))
print(hasattr(emp1, 'desg'))
setattr(emp1, 'desg' ,'manager')
print(hasattr(emp1, 'desg'))
print("added attribute",getattr(emp1, 'desg'))
#delattr(emp1,salary)
print(" is salary an attribute:",hasattr(emp1,'salary'))


