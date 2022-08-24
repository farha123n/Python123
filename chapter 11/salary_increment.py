class Employee:
    salary=1200
    salary_increment=1.5
    
    @property
    def salary_After_increment(self):

        self.salary=self.salary*self.salary_increment
        return self.salary
    @salary_After_increment.setter
    def salary_After_increment(self,value):
        self.salary_increment=value/self.salary
e=Employee()
print(e.salary_After_increment)
e.salary_After_increment=1500
print(e.salary_increment)
