# # ismlar = ['Aziz', 'Sardor', 'Ali']
# # sonlar1= [1,2,3,4,5,6,7,8,9]
# # sonlar2 = [12,23,4,56,9,8,2,5]
# #
# # print(list(map(len, ismlar)))
# # print(list(map(pow, sonlar1, sonlar2)))
# #
# # print(list(map(lambda x: x**2, sonlar1)))
#
# #1
# list1 = [3, 7, 2, 9, 5]
# list2 = [4, 6, 2, 8, 5]
# 
# min_son = list(map(min,list1, list2))
# print(min_son)
# #2
#
# s = [123, 456, 789, 321]
#
# birlar = list(map(lambda x: x % 10, s))
# print(birlar)
#
# #3
# list3 = [[3, 7, 2], [9, 5, 1], [4, 6, 8]]
#
# max_son = list(map(max, list3))
# print(max_son)
#
# for i, ism in enumerate(ismlar):
#     print(i, ism)
#
# sonlar = [1,2,3,4,5,6,7,8,9]
#
#
# natija = [i*i for i in sonlar if i %2 == 1]
#
#
# def upper(soz: str):
#     return soz.upper()
#
# print(list(map(upper, input("Vergul bilan so'z yozing: ")))).split(",")