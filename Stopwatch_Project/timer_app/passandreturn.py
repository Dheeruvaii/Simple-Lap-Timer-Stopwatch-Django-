def fun1():
    for i in 'hello':
         if(i == 'o'):
             pass
             print('pass executed')
         print(i)
fun1()
print("--------------------")


print("Return statement")
def fun2():
    for i in 'hello':
         if(i == 'e'):
            return
            print('pass executed')
            print(i)
fun2()
print("Outside the function fun2()")
    # pass vs continue
string1 = "eeeefeeefeee"
# Pass String in for loop
for value in string1:
    print("Value: ",value)
    if value == 'e':
      pass
      print('This is pass block')
print("---------------------")