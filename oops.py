class employee:
    def __init__(self):
        print("Has been initialized")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("Data/Attributes has been initialized")
    def travel(self, destination ):
        print("This travel function was called manually")
        print(f"The employee is now in {destination}")
    
sam=employee()
print(type(sam))