class B:
    def f(self):
        print("f from class B")
class A:
    def f(self):
        print("f from class A") 
class C(B, A):
    pass


if __name__ == "__main__":
    obj = C()
# lets call the f() method
    obj.f()