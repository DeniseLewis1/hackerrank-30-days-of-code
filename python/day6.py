# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    S = input()
    even_chars = ""
    odd_chars = ""

    for index in range(len(S)):
        if index % 2 == 0:
            even_chars += S[index]
        else:
            odd_chars += S[index]
            
    print(f"{even_chars} {odd_chars}")