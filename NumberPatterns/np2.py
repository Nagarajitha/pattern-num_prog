m=map(lambda sp,num, count :"-"*sp+str(num)*count,range(4,-1,-1) ,range(5,0,-1),range(1,6))
print("\n".join(list(m)))

"""
----5
---44
--333
-2222
11111

"""