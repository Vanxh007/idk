#仅此程序练手
c = 0
# Los = login or signup
print("Welcome!\nThis is a system created by uiao and vanxh,\nhope you can enjoy!")
while c ==  0:
    LoS = input('1-Login\n2-signup\n3-Exit :')
    str(LoS)
    str.lower(LoS)
    if LoS == '1':
        import loginID2
        break
    elif LoS == '2':
        import signup
        break
    elif LoS == "3":
        print("Exit!")
        break
    elif LoS == "ByVanxh":
        vanxh = open("ByVanxh.txt","r")
        mylines = vanxh.read()
        print(mylines)
        vanxh.close()
        break
    else:
        print('Please retry.')
        continue

#by zgy