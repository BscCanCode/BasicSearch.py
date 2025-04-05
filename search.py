print("Searching")
print("What would you like to do:")
print("1.Search\n2.Exit")
a=[12,3,34,12,312,324]

while True:
    try:
        n=int(input("Enter the choice:"))
        if n==2:
            print("Exit")
            break
        if 0<n<=1:
            b=int(input("Enter the element you want to search: "))
            if b in a:
                print(f"The element {b} is present in the list")
            else:
                print(f"Element {b}  is not present in the list")
        else:
            print("Enter the proper choice:")
    except:
        print("Verify your I/P and try again")
        
            
