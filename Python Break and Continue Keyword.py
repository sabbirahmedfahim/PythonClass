#break- continue
#One
i = 1
for i in range(1, 11, 1):
    if(i>7):
        break
    print(i)

#two
#break
#tricky
i = 1
for i in range(1, 11, 1):
    print(i)
    if(i>7):
        break

#three
#continue
#the continution means it will go back to loop.
i = 1
for i in range(1, 11, 1):
    if(i==5 or i==7):
        continue
    print(i)

#four
#and operation need to match two conditions at a time but here it is not possible both at the same time
i = 1
for i in range(1, 11, 1):
    if(i==5 and i==7):
        continue
    print(i)

#five
#finding even numbers using continution-for loop
i = 1
for i in range(1, 11, 1):
    if(i%2!=0):
        continue
    print(i)


#six
# Finding numbers not divisible by 3 in the range from 1 to 10
i = 1
for i in range(1, 11, 1):
    if(i%3==0):
        continue
    print(i)


#seven
#if the number divisible by 3 and 2 in the range from 1 to 10 at the same time
#it will not print because of the continuation of 'for loop'
i = 1
for i in range(1, 11, 1):
    if(i%3==0 and i%2==0):
        continue
    print(i)

#eight
#it prints 21 and 28 because there is a conditon sum>17
sum = 0
for i in range(1,8,1):
    sum = sum+i
    if(sum>17):
        print(sum)

#nine
#the code is easy to understand
sum = 0
for i in range(1,8,1):
    sum = sum+i
    if(sum>17):
        break
    print(sum)


#ten
#what if we don't maintain identation(please do not  confuse -_-, ig i need a better word)
#it prints till 21 because the break statement is after the condition

sum = 0
for i in range(1,8,1):
    sum = sum+i
    print(sum)
    if(sum>17):
        break

#eleven
#it is now very easy to understand
#the output
#it prints 21 rather than 15 because sum variable was already updated. interesting read

sum = 0
for i in range(1,8,1):
    sum = sum+i
    if(sum>17):
        break
print(sum)


#twelve
#the same code outputs different value than break. food for thought why is 28 the output
'''Here we see the continuation of the for loop. It stopped printing after >17, but the sum
 variable is being updated for every continuation of the loop.'''

sum = 0
for i in range(1,8,1):
    sum = sum+i
    if(sum>17):
        continue
print(sum)

#thirteen
#its easy. the condition checked first
sum = 0
1, 3, 6, 10, 15, 21, 28
for i in range(1,8,1):
    if(sum>17):
        break
    sum = sum + i
print(sum)

