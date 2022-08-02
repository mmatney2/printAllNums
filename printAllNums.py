def printAllNums(num):
    nums = []
    for i in range(num):
        nums.append(i)
    print(nums)
print(printAllNums(5))



list_1 = [x for x in range(10)]

def quad(list_1):
    print(list_1)
    count = 0
    for i in list_1:
        for j in range(1):
            print((i, j))
            count += 1
    print(count)
quad(list_1)

#BINARY SEARCH TREE

# def binarySearch(listData, value):
#     low = 0
#     high = len(listData) - 1
#     while low <= high:
#         mid = (low + high) / 2
#         if (listData[mid] == value):
#             return mid
#         elif (listData[mid] < value):
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# print(binarySearch([1,2,3,4], 4))

#HASH TABLE
dict_1 = [None for i in range(50)]
print(hash('Name'))
print(abs(hash('Name')% 50))
dict_1[abs(hash('Name') % 50)] = 'APPLE'
print(dict_1)