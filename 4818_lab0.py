import struct


class NutellaPacket(object):
    def __init__(self, id, secret_code, package_size, nutella_eater):
        self.id = id
        self.secret_code = secret_code
        self.package_size = package_size
        self.nutella_eater = nutella_eater
    

    def serialize(self):
        secret_code = bytes(self.secret_code, 'ascii')
        nutella_eater = bytes(self.nutella_eater, 'ascii')
        pack_output  = struct.pack("!I %ds i %ds" % (len(secret_code), len(nutella_eater)), self.id, secret_code, self.package_size, nutella_eater)
        # print(pack_output )
        # unpacked = struct.unpack("!I %ds i %ds" % (len(secret_code), len(nutella_eater)), pack_output )
        return list(pack_output)


packet = NutellaPacket(4818, 'Networks', 4096, 'Amr Mohamed Gaber')
print(packet.serialize())



# # exercise program

# class User():
#     '''
#     str() is used for creating output for end user 
#     while repr() is mainly used for debugging and development. 
#     repr’s goal is to be unambiguous and str’s is to be readable.
#     '''
#     def __init__(self, name: str, age: str):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return "user_name(\"{}\"):use_age(\"{}\")".format(self.name,self.age)
    
#     __repr__ = __str__


# users = []

# for i in range(3):
#     users.append(User(input("enter user #{} name: ".format(i+1)), input("enter user #{} age: ".format(i+1))))


# with open('Users.txt', "w") as fw:
#    for user in users:
#        #it needs to be str to write
#        fw.write(str(user)+"\n")
