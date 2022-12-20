#--本篇极为复杂，请细心阅读各行--
import time
with open("data.txt", mode = "r") as f:
    default = list(f)
IDs = default[::2] #data.txt中单数行为账号
password = default[1::2] #data.txt中双数行为密码
iop = zip(IDs,password) #将账号与密码合并成为字典
iop = dict(iop)
loginIDs = iop.keys() #字典中的账号
loginkeys = iop.values() #字典中的密码

time.sleep(2)
print("\nThis is a Login system.\n")
#帐号判定

a = 0
while a == 0:
    time.sleep(1.5)
    inputs = input("Please enter your ID :")
    str(inputs)
    userid = inputs
    inputs = (inputs + "\n")
    if inputs in loginIDs:
        print("This ID does exist.")
        break
    elif inputs not in loginIDs:
        print("This ID does not exist.")
        continue
iap = iop.items() #把{帐号：密码}(字典) 转变为 [(账号，密码)](列表)
idkeylist = list(iap)
#iap即id and password
print("------------")
#密码判定

while a == 0:
    inputss = input("Please enter your password :")
    str(inputss)
    inputss = (inputss + "\n")
    useriap = (inputs,inputss) #useriap即输入的账号与密码组合，
#iap会是[(acc1,key1),(acc2,key2)...]
    if useriap == idkeylist[2]:
        print("Admin login.")
        a = a + 2
        break
    elif useriap not in iap:
        print("Wrong password.")
        continue
    elif useriap in iap:
        print("Login succes.")
        break

while a == 2:
    adminchoice = input("1-Check user info\n2-Check usertxt\n3-Exit :")
    str(adminchoice)
    if adminchoice == "1":
        for userinfo in idkeylist:
            userinfo = "".join(userinfo)
            userinfo =  userinfo.strip("\n")
            print(userinfo)
    elif adminchoice == "2":
        admin_checkno = input("User number :")
        admin_choose_txt = int(admin_checkno) - 1
        admin_check = open(IDs[admin_choose_txt] + ".txt", mode = "r")
        admin_check_txt = admin_check.read()
        print(admin_check_txt)
        admin_check.close()
        break
    elif adminchoice == "3":
        break
#询问是否要修改用户的txt

while a == 0:
    readorwrite = input("1-Read txt\n2-Write txt\n3-Exit\n4-Back to home :\n")
    str(readorwrite)
    if readorwrite == "1":
    	readtxt = open(userid + ".txt", mode = "r", encoding = "utf-8")
    	txt = readtxt.read()
    	print(txt)
    	if txt == "":
            print("It is a empty txt.")
            readtxt.close()
    elif readorwrite == "2":
        writetxt = open(userid + ".txt", mode = "a+", encoding = "utf-8")
        userwrite = input("Please enter what you want to write :")
        print("--------------------")
        str(userwrite)
        userwrite = (userwrite + "\n")
        print("This is your writing :" , userwrite)
        print("\n")
        writetxt.write(userwrite)
        writetxt.close()
    elif readorwrite == "3":
        break
    elif readorwrite == "4":
        import home
        break
    else:
        print("Our system still need to update.")
        continue
#by zgy
f.close()