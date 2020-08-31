list1 = list();
list2 = list();

def merge_two_sorted_list(list1, list2):
    n1 = len(list1);
    n2 = len(list2);
    list3 = []
    i = 0
    j = 0
    while(i < n1 and j < n2):
        if(list1[i] < list2[j]):
           list3.append(list1[i])
           i = i+1   # no support of i++
        else:
           list3.append(list2[j])
           j = j+1
    if(i < n1):
      list3.append(list1[i])
    if(j < n2):
      list3.append(list2[j])
   
    return list3

# supported python3, test in online 
print("Enter sorted list-1")
list1 = [int(i) for i in input().split(" ")]   # split is str method
print("Enter sorted list-2")
list2 = [int(i) for i in input().split(" ")]   # split is str method

list3 = merge_two_sorted_list(list1, list2)
print(list3)
