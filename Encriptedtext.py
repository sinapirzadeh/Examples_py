while True:
    print('Choose Your Otions:\n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit')
    choose = input("your Choose : ")
    if choose == '1':
        plain_text = input('text : ')
        encrypted_text = ''
        for c in plain_text:
            x = ord(c) * 2 + 3
            encrypted_text += chr(x)
        print('encrypted text :', encrypted_text)
        print('-'*30 + '\n')
    elif choose == '2':
        encrypted_text = input('text : ')
        plain_text = ''
        for c in encrypted_text:
            x = (ord(c) - 3) // 2
            plain_text += chr(x) 
        print('Plain text :', plain_text)
        print('-'*30 + '\n') 
    elif choose == '3':
        break
    else:
        print('your choose is Wrong!')
