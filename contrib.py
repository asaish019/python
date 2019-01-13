#calculate total contribution per person.

def food(f):
    tip=0.1*f
    f=f+tip
    fperson=f/num
    return fperson

def movie(m):
    return m/num
num=int(input("no. of friends: "))
ftotal=int(input("Spent on food: "))
mtotal=int(input("Spent on movie: "))

x=food(ftotal)
y=movie(mtotal)
print("the per person total is: :",x+y)
