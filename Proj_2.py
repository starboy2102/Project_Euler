"""
Problem - 02
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
a=[1,2]
c=[]
while 1:
    b = a[-1]+a[-2]
    a.append(b)
    if a[-1] >= 4000000:
        break
for i in a:
    if i%2 ==0:
        c.append(i)
print(sum(c))

