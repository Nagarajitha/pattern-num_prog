m=map(lambda sp,num, count :"-"*sp+str(num)*count,range(4,-1,-1) ,range(1,6),range(1,6))
print("\n".join(list(m)))

"""
----1
---22
--333
-4444
55555

"""