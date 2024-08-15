# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

phoneBook = {}

for i in range(n):
    name, phoneNumber = input().split()
    
    phoneBook[name] = int(phoneNumber)
    
while True:
    try:
        query = input()
        if query not in phoneBook:
            print("Not found")
        else:
            print(f"{query}={phoneBook[query]}")
    except:
        break