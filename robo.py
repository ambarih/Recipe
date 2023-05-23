class Robo:
    def __init__(self,name,id,version):
        self.name=name
        self.idNumer=id
        self.ver=version
       
    def fun(self,workingHorus):
        self.workingHours =workingHorus
        print("i am working from last ",workingHorus)
        if(workingHorus >=10 ):
            print("please charge me")
        else:
            print("I can be able work,i dont have any issues")
    
    # def cleaning():
    #     # pass
    #     a=input( print("enter the area: "))
        


a=Robo("Chiti",4,2)
a.fun(9)
# a.cleaning()
