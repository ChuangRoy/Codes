import pdb
class A_Object (object):
    def __init__ (self , a , b , c) :
        self.a = c
        if a == b:
           print("??????")
           print("A==B")
        else :
           print("!!!!!!")
           print("a != B")
    def __nothing__ (self) :
        print(self.a)

if __name__ == "__main__":
    A = A_Object (1 , 1 , 2)
    A.__nothing__()
    pdb.set_trace()
