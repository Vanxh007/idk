# Created on 2019309.

print ('Hello World!')

import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
itchat.auto_login(hotReload=True)
itchat.run()
