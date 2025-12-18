#1
import numpy as np
print( f"1. version : {np.__version__}")
#2
arr2 = np.arange(0,21)
print(f"2. {arr2}")
#3
arr3 = np.full((3,3),True)
print(f"3. {arr3}")
#4
arr4 = np.arange(0,10)
dk = arr4 % 2 == 1
print(f"4.  mang cu: {arr4}")
print(f"    mang moi : {arr4[dk]}")
#5
arr5 = arr4.copy()
for i in range(len(arr5-1)):
    if arr5[i] % 2 == 1:
        arr5[i] = -1
print(f"5.  mang cu: {arr4}")
print(f"    mang moi: {arr5}")
#6
arr6 = arr4.copy()
print(f"6.  mang cu: {arr6}")
copyarr6 = arr6.copy()
for i in range(len(copyarr6-1)):
    if copyarr6[i] % 2 == 1:
        copyarr6[i] = -1
print(f"    mang moi: {copyarr6}")
print(f"    mang cu: {arr6}")
#7
arr7 = arr4.copy()
print(f"7.  mang cu: {arr7}")
print(f"    mang moi: {arr7.reshape(2,5)}")
#8
arr8 = np.arange(0,10).reshape(2,5)
brr8 = np.full((2,5),1)
print(f"8. A: {arr8}")
print(f"   B: {brr8}")
print(f"kq : {np.concatenate((arr8,brr8), axis = 0)}")
#9
arr9 = np.arange(0,10).reshape(2,5)
brr9 = np.full((2,5),1)
print(f"9. A: {arr9}")
print(f"   B: {brr9}")
print(f"kq : {np.concatenate((arr9,brr9), axis = 1)}")
#10
arr10 = np.array([1,2,3])
arr10_new0 = np.repeat(arr10,3)
print(f"10. {arr10}")
print(f"A: {arr10_new0}")
arr10_new1 = np.tile(arr10, 3)
print(f"B: {arr10_new1}")
arr10_new2 = np.tile(arr10, (1,3))
print(f"C: {arr10_new2}")
#11
arr11_1 = np.array([1,2,3,2,3,4,3,5,6])
arr11_2 = np.array([7,2,10,2,7,4,9,4,9,8])
print(f"11. {np.intersect1d(arr11_1,arr11_2)}")
#12
arr12_1 = np.array([1,2,3,4,5])
arr12_2 = np.array([5,6,7,8,9])
print(f"12. {np.setdiff1d(arr12_1,arr12_2)}")
#13
arr13_1 = np.array([1,2,3,2,3,4,3,4,5,6])
arr13_2 = np.array([7,2,10,2,7,4,9,4,9,8])
print(f"13. {np.where(arr13_1 == arr13_2)}")
#14
arr14 = np.array([2,6,1,9,10,3,27])
index_14 = np.logical_and(arr14>=5, arr14<=10)
print(f"14. {arr14[index_14]}")
#15 a
def maxx(x,y):
    if x>=y:
        return x
    else:
        return y
arr15_1 = np.array([5,7,9,8,6,4,5])
arr15_2 = np.array([6,3,4,8,9,7,1]) 
pair_max = np.vectorize(maxx)
print(f"15a. {pair_max(arr15_1,arr15_2)}")
#15 b
arr15_3 = np.array([5,7,9,8,6,4,5])
arr15_4 = np.array([6,3,4,8,9,7,1]) 
where_15b = np.where(arr15_3 > arr15_4, arr15_3, arr15_4)
print(f"15b. {where_15b}")
#16
arr16 = np.arange(9).reshape(3,3)
arr16_new = arr16[:,[1,0,2]]
print(f"16. {arr16_new}")
#17
arr17 = np.arange(9).reshape(3,3)
arr17_new = arr17[[1,0,2],:]
print(f"17. {arr17_new}")
#18
arr18 = np.arange(9).reshape(3,3)
arr18_new = arr18[::-1,:]
print(f"18. {arr18_new}")
#19
arr19 = np.arange(9).reshape(3,3)
arr19_new = arr19[:,::-1]
print(f"19. {arr19_new}")
#20
arr20 = np.random.uniform(5,10,(5,3))
print(f"20. {arr20}")
#21
arr21 = np.random.randint(1,50,(5,3))
where_21 = np.where(arr21 > 30, 30, np.where(arr21<10,10,arr21))
print(f"21. {where_21}")
#22
arr22 = np.random.randint(1,50,(5,3))
flatten_22 = arr22.flatten()
index_22 = np.argpartition(flatten_22,-5)[-5:]
print(f"22. {flatten_22}")
print( index_22)
print(flatten_22[index_22])
#23
arr23_1 = np.arange(3)
arr23_2 = np.arange(3,7)
arr23_3 = np.arange(7,10)
arr23  = np.array([arr23_1,arr23_2,arr23_3],dtype= object)
print(f"23. {arr23.flatten()}")
#24
arr24 = np.random.randint(1, 10, [5,3])
arr24_new = np.amax(arr24,axis= 1)
print(f"24. {arr24}")
print(arr24_new)
#25
arr25 = np.random.randint(1, 10, [5,3])
print(f"25. {arr25}")
arr25_new1 = np.amax(arr25,axis= 1)
arr25_new2 = np.amin(arr25,axis= 1)
print(arr25_new2/arr25_new1)
#26
#27
arr27 = np.array([1,2,3,4,5])
brr27 = np.array([4,5,6,7,8])
dist = np.linalg.norm(arr27-brr27)
print(f"27. {dist}")
