n = int(input("Enter the number of elements: ")) 
arr = list(map(int, input("Enter the elements: ").split()))
unique_numbers = sorted(set(arr), reverse=True)  
if len(unique_numbers) >= 2:
    print(unique_numbers[1])




         

        
