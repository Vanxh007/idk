import os
import time
#开场白
time.sleep(2)
print('\nThis is a signup system,\n')
time.sleep(1.3)
print("your ID must be 8 string.\n")
time.sleep(1)
with open("data.txt", mode = "r")as checking:
	checkopass1 = list(checking)
checkopass2 = checkopass1[::2]

b = 0
#账号注册
while b == 0:
  time.sleep(1.4)
  opass = input('Please enter your ID :') #Set ID
  str(opass)
  opass2 = (opass + "\n")
  if len(opass) > 8:
    time.sleep(1.4)
    print('\nYour ID number is too long.')
    continue
  elif len(opass) < 8:
    time.sleep(1.4)
    print('\nYour ID number is too short.')
    continue
  elif opass2 in checkopass2:
    print("\nLoading...")
    time.sleep(2.3)
    print("\nYour ID number has been signuped.")
    continue
  elif len(opass) == 8 and opass2 not in checkopass2:
    time.sleep(1.5)
    print("\nThis ID is avalible.\n")
    break
print('\nYour ID is: ' + opass)

#账号注册完成，开始确认密码
oacc = ' '
time.sleep(1.5)
print("\nPassword must be 6 string.\n")
while len(oacc) != 6:
  time.sleep(1.5)
  oacc = input('Please enter your password :') #Set Key
  str(oacc)
  if len(oacc) > 6:
    time.sleep(1.5)
    print('\nYour password is too long.\n')
    continue
  elif len(oacc) < 6:
    time.sleep(1.5)
    print('\nYour password is too short.\n')
    continue

#密码注册完成
ID = opass
key = oacc

#装b
time.sleep(1.5)
print('\nLoading')
for i in ('...'):
  time.sleep(1.5)
  print(i)
time.sleep(3)
#装b

print('\nDone!\n')
time.sleep(1.5)
print('Your account is created successfully!')
#把用户资料写入data.txt

f = open('data.txt', mode='r', encoding='utf-8')
f.close()
with open('data.txt', 'a+', encoding = 'utf-8') as f:
  f.write(ID + '\n')
  f.write(key + "\n")

#为用户创建专属txt
usertxt = open(ID + ".txt",mode = 'a', encoding = "utf-8")
usertxt.close()

#询问登入与否
a = 0
while a == 0:
  time.sleep(1.5)
  gotologin = input("Would you want to login your account?\nYes or no :")
  str.lower(gotologin)
  if gotologin == ("yes"):
    import loginID2
    break
  elif gotologin == ("no"):
    break

#by zgy