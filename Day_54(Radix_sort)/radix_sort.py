def counting_sort_for_radix(arr,exp):
    n = len(arr)
    output = [0] * n
    count =  [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        digit = index % 10 
        count[digit]+=1
        
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = arr[i] // exp 
        digit = index % 10
        
        output[count[digit]-1] = arr[i]
        
        count[digit] -= 1
        i -= 1
        
    for i in range(n):
        arr[i] = output[i]
           
def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1 
    
    while max_val // exp>0:
        print("\nPass for digit position (exp={})".format(exp))
        
        counting_sort_for_radix(arr,exp)
        print("List after pass: " ,arr)
        exp *= 10
    return arr 

if __name__ == "__main__": 
    data = [55,20,81,76,92,43,35,17]
    print("Original Array: ",data)
    sorted_data = radix_sort(data)
    print("\n Sorted Array:",data)

