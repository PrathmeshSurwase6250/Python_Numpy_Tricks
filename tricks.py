import numpy as np 

rand = np.random.randint(1,101,15)
print(rand)

print(np.sort(rand))

b = np.random.randint(1,100,24).reshape(6,4)
print(b)
print(np.sort(b))
print(np.sort(b,axis=0))


print(np.append(b, np.ones((b.shape[0], 1)), axis=1))

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
c = np.concatenate((a,b), axis=0)
print(c)
c = np.concatenate((a,b), axis=1)
print(c)

e = np.array([1,1,1,2,2,3,3,4,4,5,6,7,7,4])
print(np.unique(e))


a = np.random.randint(1,101,30)
print(a)

# a = np.expand_dims(a , axis=1)
# print(a)

# print(np.where(rand > 50))

# print(np.where(a>50 , 0 , a))

# print(np.argmax(rand))
b = np.random.randint(1,101,24).reshape(6,4)
# print(np.argmax(b,axis=0))
# print(np.argmin(b , axis=1))

# print(np.cumsum(b))
# print(np.cumprod(b))

# print(np.percentile(b,50))
print(np.histogram(b,bins=[0,50,100]))
 

salary = np.array([20000,40000,60000,100000])
exp = np.array([1,2,3,4])
c = np.corrcoef(salary,exp)
print(c)

items = np.array([10,20,30,40,50,60,70,80,90])
print(np.isin(b,items))
print(np.flip(items))
np.put(items , [0,1] , [200000,500000])
print(items)

print(np.delete(items,[0,1]))