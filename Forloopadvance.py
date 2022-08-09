mul=1
for i in range(1,11):
    mul=mul*i
print(mul)



print("-----------------------------------------------------------------------");


num=12345
sum=0
for i in range(len(str(num))):
    temp=num%10  #extract the last number and print the exclude num
    print(temp)
    num=num//10  # avoid the last number and print num
    print(num)
    sum+=temp  ##add exclude number
    print(sum)
