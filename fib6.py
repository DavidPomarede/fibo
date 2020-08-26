def move(f,t) :
    print("Move disc from {} to {}!".format(f,t))

## print(move('A','C'))

def moveVia(f,v,t) :
    move(f,v)
    move(v,t)

 print(moveVia("A","B","C"))


##def foo(x) :
##    foo(x)

## print(foo('dfj'))


def hanoi(n,f,h,t) :
    if n==0 :
        pass
    else :
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

print(hanoi(4,"A","B","C"))



