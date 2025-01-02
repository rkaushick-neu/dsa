list_students = ['Peele', 'Etna', 'Krakatoa', 'Agung', 'Vesuvius', 'St. Helens']

def insertion_sort(list_students):
    n = len(list_students)
    for i in range(0, n):
        for j in range(i, 0, -1):
            if(list_students[j] < list_students[j-1]):
                # swap
                pass
            else:
                break