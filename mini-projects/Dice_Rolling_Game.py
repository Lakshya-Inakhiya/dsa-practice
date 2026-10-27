import random
dice = [ n for n in range(1,7)]
is_running = True
count = 0
print("**************Dice Rolling Mini Game**************")
while is_running:
    try:
        n = int(input("Enter Number of Dices to throw ( 0 to quit): "))
        print("*"*50)
    except ValueError:
        print("Enter Valid Input")
        print("*"*50)
        continue
    result = []
    if n == 0:
        print("Bye")
        print("*"*50)
        is_running = False
        continue
    elif n<0:
        print("Enter Valid Input")
        print("*"*50)
        continue
    for _ in range(n):
        result.append(random.choice(dice))
    print(result)
    total = 0
    for v in result:
        total += v
    avg = total / n
    print("Sum:", total, "Average:", avg)
    print("*"*50)

        
