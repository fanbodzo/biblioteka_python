
class User():
    def __init__(self,id,username,password,name,surname,status):
        #protected
        self._id=id
        self._username=username
        self._password=password
        self._name=name
        self._surname=surname
        self._status=status
        
    def wyswietl_inf(self):
        print(self._id,self._username,self._password,self._name,self._surname,self._status)
        
    def wyswietl_role(self):
        print(self._status)
        
class Regular_user(User):   #dziedziczenie z klasy user + polimorfyzm  
    pass

class Admin(User):  #dziedziczenie z klasy user + polimorfyzm  
    pass
    
admin =Admin(1,'admin','123','imie','nazwisko','admin')
user =Regular_user(2,'filip','123','imie','nazwisko','user')

admin.wyswietl_inf()
user.wyswietl_inf()