#!usr/bin/python
# -*- coding: utf-8 -*-
import itchat, time

#http://www.runoob.com/python/python-if-statement.html

if True:
    print("true");
else:
    print("else");
#20190124
if False:
    print("flase");



#https://www.cnblogs.com/wang-li/p/9744502.html
#利用itchat给女朋友定时发信息



#itchat.auto_login(loginCallback=lc, exitCallback=ec)
itchat.auto_login();

def findFriend(NickName):
    for firend in itchat.get_friends():
        #print firend["NickName"];
        if firend["NickName"]==NickName:
            return firend;


#定义用户的昵称
nickName=u'点点水';
#查找用户的userid
#user = itchat.search_friends(send_userid);
user = findFriend(nickName);
itcaht_user_name="";
if user is not None:
    print (user);
    itcaht_user_name=user['UserName'];

if user is not None and itcaht_user_name !='':
    #利用send_msg发送消息
    itchat.send_msg(u'这是一个测试',toUserName=itcaht_user_name)
    time.sleep(1000)

itchat.logout()    #强制退出登录   
  
# 原文：https://blog.csdn.net/enweitech/article/details/79585043 
