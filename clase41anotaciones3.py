class employee:
    name: str
    age: int
    salary: float

    def __init__(self,name:str,age:int,salary:float):
        self.name=name
        self.age=age
        self.salary=salary

    def introduce(self)->str:
        return f"Hola,me llamo {self.name}, tengo {self.age} años y gano {self.salary} de salario"
    
employee1=employee("Carlos",30,3500.0)
print(employee1.introduce())