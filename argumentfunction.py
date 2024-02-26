def add(x,y):
    print(x+y)
def mul(x,y):
    print(x*y)
def arg(func,x,y):
    func(x,y)
'''def hi(fun,func):
    fun(func(x,y),x,y)'''
    
    
a=arg(add,mul,10,20)
#a=hi(arg(add(10,20))
