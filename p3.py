# code here
# initializing lists
t1 = [3,4,5,1]
t2 = [6,7,2,8]

print ("Original list : " + str(t1))
print ("Original list  : " + str(t2))
  
rl = []
for i in range(0, len(t1)):
    rl.append(t1[i] + t2[i])
  
print ("Added list is : " + str(rl))

# code here
name_surname = "Seaim Tanzimul Haque".split(" ")
to_output1 = name_surname[0]  
to_output2 =name_surname[-1]
print('First name:',to_output1)
print('Last name:',to_output2)

a = 21
print(a)

a = input('Enter a value: ') # always returns string
print('The given value is '+ a)
print(type(a))

while True:
      a = input('Enter your Birth Year:')
  if a.isdigit():
    print('You are ' + str(2022-int(a)) + ' years old')
    print(2022-int(a))
    break
  print('WRONG INPUT')
  
  # indent
i = 2
if i < 5: # () not required, {} not required
  print('okay')
  print('fine')
else:
  print('bad')
  print('not okay') # will be executed in each run
  
  x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    # code here
m = float(input("Enter your marks "))

if m >= 100:
    print("Grade: A+")
elif m >= 90 and m < 100:
    print("Grade: A")
elif m >= 70 and m < 80:
    print("Grade: B+")
elif m >= 60 and m < 70:
    print("Grade: B")
elif m >= 50 and m < 60:
    print("Grade: C+")
elif m >= 40 and m < 50:
    print("Grade: C")
else:
    print("Grade: F")
    
    
    # code here
 
s = int(input("start from : "))
e = int(input("End : "))
 
for n in range(s, e + 1):
    
    if n % 2 == 0:
        print(n)
        print(end = " ")