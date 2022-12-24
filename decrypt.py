#number of columns
t = int(input('Enter secret key :'))
if t == 0:
    print('_')
else:
    string = input('Enter your message: \n')
    list0 = list(string)
    length = len(list0)
    print('Your message is of length: ', length, '\n')
    #number of rows
    block = length // t
    if block == 0 :
        print('Invalid key! Try again later!')
    else:
        list1 = []
        for i in range(block):
            I = i*(t)
            I1 = (i+1)*(t)
            if i%2 == 0:
                for j in range(I,I1):
                    list1.append(list0[j])
            else:
                for j in range(1, t +1):
                    list1.append(list0[I1-j])
        answer = []
        def decrypt(list9, r, s):
            j= 0
            while j < s:
                x = j*(t) + r
                d = list9[x]
                answer.append(d)
                j += 1
        for k in range(t):
            decrypt(list1, k, block)
        #list to string
        strans = ' '
        for ele in answer:
            strans += ele
        print(strans)

   

