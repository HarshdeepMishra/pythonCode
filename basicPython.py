
''' 
    Question 1: Print functions question .
    Example input n = 6
    
    Expected output = 12345
'''
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
'''
    Question 2: Python if else question .
    Task :Given an integer, , perform the following conditional actions:
    If  is odd, print Weird
    If  is even and in the inclusive range of 2 to 5 print Not Weird
    If  is even and in the inclusive range of 6 to 20 print Weird
    If  is even and greater than 20 print Not Weird
'''
if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0 and 2<=n<=5:
        print("Not weird")
    elif n%2 == 0 and 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")


if __name__ == "__main__":
    
    n = int(input())
    t = tuple(map(int, input().split()))
    
print(hash(t))

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = 0 
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scorelist = student_marks[query_name]
    
    for i in scorelist:
        total += i
    

    average = total/len(scorelist)
    print("{:.2f}".format(average))
