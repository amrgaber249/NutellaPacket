class User():
    '''
    str() is used for creating output for end user 
    while repr() is mainly used for debugging and development. 
    repr’s goal is to be unambiguous and str’s is to be readable.
    '''
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return "user_name(\"{}\"):use_age(\"{}\")".format(self.name,self.age)
    
    __repr__ = __str__




users = []

for i in range(3):
    users.append(User(input("enter user #{} name: ".format(i+1)), input("enter user #{} age: ".format(i+1))))


with open('Users.txt', "w") as fw:
   for user in users:
       #it needs to be str to write
       fw.write(str(user)+"\n")
