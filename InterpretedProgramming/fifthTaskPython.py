list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
print(f"Количество повторяющихся чисел в списках: {len(set(list1) & set(list2))}")