# for num in [20,111,9,87,4,44]:
#     # skipping the interation when the number is even
#     if num%2==0:
#         continue
#     #this statement wil be skipped for all even numbers
#     print(num)
    
    # even num
# for num in [20,111,9,27,4,44]:
#         if num %3 ==0:
#             continue
#         print(num)


# for i in range(5):
#     for j in range(5):
#         if i==3:
#           break
#     if i ==3:
#           break
#     print(i,j)
    
    # Fibonacci series up to n terms

n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")

while count < n:
    print(a)
    a, b = b, a + b
    count += 1
