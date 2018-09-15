#!/usr/bin/env python
# _*_ coding:utf-8 _*_
name = "我的名字叫二哈请多多关照！"
student_no = "我的学号是000001"
price = 8.5
money_all = 1000
print(name)
print(student_no)
print("苹果的单价为%.1f元/斤"%(price))
weight = int(input("二哈同学，请问您要买多少斤苹果？"))
money = price * weight
scale = (money_all - money) / 1000 * 100
print("苹果单价为%.1f元/斤，您买了%.1f斤苹果，二哈同学您需要支付金额为%.2f元！！"%(price,weight,money))
print("二哈同学剩余的钱大约是总额的%.f%%。"%(scale))