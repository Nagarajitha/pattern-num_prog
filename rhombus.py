

m=map(lambda sp,st:('_'*sp)+('*'*st),range(3,-1,-1) ,range(1,8,2))
print("\n".join(list(m)))
m=map(lambda sp,st:('_'*sp)+('*'*st),range(1,4) ,range(5,0,-2))
print("\n".join(list(m)))


"""

___*
__***
_*****
*******
_*****
__***
___*


"""