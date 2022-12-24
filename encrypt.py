t = int(input('Enter the secret key: '))
if t == 0:
    print('_')
else:
    string = input('Enter your message, to display spaces or blanks, input _. Type here: \n')
    list01 = list(string)
    length1 = len(list01)
    v = length1 % t
    if v == 0:
        list0 = list01
        length = len(list0)
        block = length // t
        list1 = []
        def encrypt(list9, r, s):
            j = 0
            while j < s:
                x = j*(block) + r
                d = list9[x]
                list1.append(d)
                j += 1
        for k in range(block):
            encrypt(list0, k, t)
        answer = []
        for i in range(block):
            I = i*(t)
            I1 = (i+1)*(t)
            if i%2 == 0:
                for j in range(I,I1):
                    answer.append(list1[j])
            else:
                for j in range(1, t+1):
                    answer.append(list1[I1-j])
        strans = ' '
        for ele in answer:
            strans += ele
        print(strans)
    else:
        list0 = list01
        h = 1
        while h <= t-v:
            list0.append('_')
            h += 1
        print('To make your message sendable, we are appending ', t-v, ' "_" after the end of your msg.')
        length = len(list0)
        block = length // t
        list1 = []
        def encrypt(list9, r, s):
            j = 0
            while j < s:
                x = j*(block) + r
                d = list9[x]
                list1.append(d)
                j += 1
        for k in range(block):
            encrypt(list0, k, t)
        answer = []
        for i in range(block):
            I = i*(t)
            I1 = (i+1)*(t)
            if i%2 == 0:
                for j in range(I,I1):
                    answer.append(list1[j])
            else:
                for j in range(1, t+1):
                    answer.append(list1[I1-j])
            strans = ' '
        for ele in answer:
            strans += ele
        print(strans)
            
