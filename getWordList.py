with open('./customPass.txt','r') as f:
    wordLists=f.readlines()
    for i in range(len(wordLists)):
        words=wordLists[i]
        addMethod = ord(words[0]) & ord(words[2])
        checkAdd=hex(addMethod)
        if checkAdd == '0x60':
            orMethod = ord(words[1]) | ord(words[4])
            checkOr=hex(orMethod)
            if checkOr == '0x61':
                xorMethod = ord(words[3]) ^ ord(words[5])
                checkXor=hex(xorMethod)
                if checkXor == '0x6':
                    print(words,end="")