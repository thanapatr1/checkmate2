# a=['0']*6
first=[]
second=[]
third=[]
fourth=[]
fifth=[]
sixth=[]
for i in range(97,123):
    for j in range(97,123):
        addMethod = i & j
        checkAdd=hex(addMethod)
        if checkAdd == '0x60':
            # print("==========")
            # print(f"for first char is {chr(i)} and third char is {chr(j)}")
            # a[0] = chr(i)
            first.append(chr(i))
            # a[2] = chr(j)
            third.append(chr(j))
        orMethod = i | j
        checkOr=hex(orMethod)
        if checkOr == '0x61':
            # print("==========")
            # print(f"for second char is {chr(i)} and fifth char is {chr(j)}")
            # a[1] = chr(i)
            second.append(chr(i))
            # a[4] = chr(j)
            fifth.append(chr(j))
        xorMethod = i ^ j
        checkXor=hex(xorMethod)
        if checkXor == '0x6':
            # print("==========")
            # print(f"for fourth char is {chr(i)} and sixth char is {chr(j)}")
            # a[3] = chr(i)
            fourth.append(chr(i))
            # a[5] = chr(j)
            sixth.append(chr(j))
        # print(a)
        # print("".join(a))
 
        #hint s/d/s/


print("first possible characters are => "+"".join(set(first)))
print("second possible characters are => "+"".join(set(second)))
print("third possible characters are => "+"".join(set(third)))
print("fourth possible characters are => "+"".join(set(fourth)))
print("fifth possible characters are => "+"".join(set(fifth)))
print("sixth possible characters are => "+"".join(set(sixth)))
