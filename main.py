import random
list = [random.randint(0, 100) for x in range(1000)]
print("Mode of List A is % s" % (max(set(list), key = list.count)))
answer = input("Press 1 then enter to see list, Press enter to exit") 
if answer == "1": 
    print(list)
    input('press enter to exit')
if answer == "2":
    quit("bye")
