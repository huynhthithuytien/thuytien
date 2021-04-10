import math
import random
class PERSON:
    def __init__(self,STT,name,age,gender):
        sefl.STT=n
        self.name =name
        self.age = age
        self.gender =gender                                                  
    def ho_ten(self):
        for i in range(0,self.STT):
            hoten=str(input("nhap ho ten sinh vien thu {} ": ".format(i+1)))
            self.name.append(hoten)
        return self.name
    def tuoi(self):
        for i in range(0,self.STT):
            tuoisv=int(random.randrange(17,25))
            self.age.append(tuoisv)
            return self.age
    def gioi_tinh(self):
        for i in range(0,self.STT):
            sex=str("sinh vien thu{} : ".format(i+1))
            self.gender.append(sex)
            return self.gender
class studen(Person):
   def __init__(self,n):
       super().__init__(n)
       self.id=[]
       self.cl=[]
       self.grade=[]
       self.danhsach=[]
   def nhap_id(self):
          for i in range(0,self.STT):
              idcard=int(input("nhap so id cho sinh vien thu {} :".format(i+1)))
              self.id.append(idcard)
              return self.id
    def lop_hoc(self):
        for i in range(0,self.STT):
            tenlop=sstr(input("nhap ten lop cua sinh vien thu {} :".format(i+1)))
            self.cl.append(tenlop)
        return self.grade
    def diem_so(self):
        for i in range(0,self.STT):
            diem=int(input("nhap so diem cua sinh vien thu {} :".format(i+1)))
            self.grade.append(diem)
        return self.grade
    def danh_sach(self):
        a=[]
        for j in range(0,self.STT):
            for i in range(0,self.STT):
    
    def age(self):
        return self.age
    def name(self):
        return self.name
    def gender(self):
        return self.gender
class COMPLEX:
    def__init__(self,thuc,ao):
        self.real=thuc
        self.image=ao
    def module_sophuc(self):
        z=math.sqrt(self.real)**2+(self.image)**2
        return z
        

    
              
        
    