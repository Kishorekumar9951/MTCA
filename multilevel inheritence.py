class A:
    def first_method(self):
        print("method of class A....")

class B(A):
    def second_method(self):
        print("method of class B....")
        super().first_method()


        
##class C(A,B):
##    def third_method(self):
##        print("method of class C....")
##
##if __name__=="__main__":
##    ob=C()
##    ob.first_method()
####  ob.second_method()
##    ob.third_method()
ob=B()
ob.first_method()
