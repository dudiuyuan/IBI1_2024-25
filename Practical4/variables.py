a=15
b=60+15
c=a+b
d= 60+30
e=5
f=d+e
if c >= f:                                         #easy to know which is longer
    print("c is longer, while f is quicker")
else:
    print("f is longer, while c is quicker")       #That's it!


X = True
Y = False
W = X and Y

# Truth table for W:
# X     Y     W
# True  True  True
# True  False False
# False True  False
# False False False

print(W) #The table shows that W is True only when both X and Y are True. In all other cases, W is False.

