# Задание 1 - преобразовать список в словарь
def ListToDict():
    aList = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']
    print({value: [ind for ind, x in enumerate(aList) if x == value] for value in aList})
ListToDict()

#Задание 2 - Метрика Жаккара
def Jaccard():
    setA = set({1,2,3,5})
    setB = set({1,4,3,5})
    count = 0
    for item in setA:
         if item in setB:
             count += 1
    print(count / (len(setA) + len(setB) - count))
Jaccard()
