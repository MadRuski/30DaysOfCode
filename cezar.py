while True:
    unos=str(input("Press E to encrypt or press D to decrypt: "))
    abc=['A','B','C','D','E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if unos.lower()=='e':
        mess=list(str(input('What is your message: ')))
        for i in range(len(mess)):
            if mess[i] not in abc:
                mess[i]=mess[i].upper()
                mess[i]=abc[(abc.index(mess[i])+3)%26].lower()
            else:
                mess[i]=abc[(abc.index(mess[i])+3)%26]

    if unos.lower()=='d':
        mess=list(str(input('What is your message: ')))
        for i in range(len(mess)):
            if mess[i] not in abc:
                mess[i]=mess[i].upper()
                mess[i]=abc[(abc.index(mess[i])+23)%26].lower()
            else:
                mess[i]=abc[(abc.index(mess[i])-23)%26]
    print(''.join(mess))