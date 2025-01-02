# list_students = ['Peele', 'Etna', 'Krakatoa', 'Agung', 'Vesuvius', 'St. Helens']
list_numbers = [5, 3, 2, 1, 4, 6]

def sort(list_items):
    n = len(list_items)
    for i in range(0, n):
        min = i
        for j in range(i, n):
            # find minimum
            if(list_items[j] < list_items[min]):
                min = j
            # print(list_items, j)
        # swap a[min] and a[i]
        temp = list_items[i]
        list_items[i] = list_items[min]
        list_items[min] = temp
        # print(list_items)

print(list_numbers)
sort(list_numbers)
print(list_numbers)