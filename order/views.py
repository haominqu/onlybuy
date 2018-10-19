from django.shortcuts import render
from django.http import request, response, HttpResponse
from userinfo.models import *
from .models import *
import datetime
from django.db import DatabaseError
import logging
from django.core import serializers
import json
# Create your views here.
# goods = [
#     {"id":5,"title":"诺基亚7750蓝色","price":1000.00,"desc":"全面屏，2000万后置摄像头","amount":2,"trprice":1000.00},
#     {"id":2,"title":"iphoneXs金色","price":8700.00,"desc":"全面屏，2000万后置摄像头","amount":3,"trprice":8700.00},
#     {"id":3,"title":"iphoneXs玫瑰金","price":8700.00,"desc":"全面屏，2000万后置摄像头","amount":2,"trprice":8700.00},
#     {"id":4,"title":"诺基亚7750黑色","price":1000.00,"desc":"全面屏，2000万后置摄像头","amount":1,"trprice":1000.00},
# ]

def add_order(request):
    if request.method == "POST":
        user = request.user
        ads = request.POST.get("ads", "")
        tomoney = request.POST.get("tomoney", "")
        trmoney = request.POST.get("trmoney", "")
        bank = request.POST.get("bank", "")
        goods = request.POST.get("goods", "")
        dealtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        orderNo =dealtime
        mtomoney = 0
        amount = 0
        # 计算总金额是否一致,总数量
        for good in goods:
            mtomoney = mtomoney + good["price"]
            amount = amount +good["amount"]
        if mtomoney != tomoney:
            return HttpResponse(json.dumps({"result":False,"msg":"金额不一致"}))

        order = Order.objects.create(orderNo=orderNo, ads=ads, tomoney=tomoney, trmoney=trmoney, amount=amount,
                                     bank=bank, dealtime=dealtime, status=0, user=user)
        glist = list()
        for good in goods:
            glist.append(OrderGoods(title=good["title"],price=good["price"],desc=good["desc"],amount=good["amount"],trprice=good["trprice"],order=1))
        OrderGoods.objects.bulk_create(glist)
        return HttpResponse(json.dumps({"result": True, "msg": "订单成功"+order.orderNo}))

    elif request.method == "GET":
        return render(request,'login.html')


def order_list(request):
    if request.method == "GET":
        user = request.user
        orderlist = Order.objects.filter(user_id=user.id)
        orderlists = []
        for order in orderlist:
            orderlistt = {}
            orderlistt['orderNo'] = order.orderNo
            orderlistt['ads'] = order.ads
            orderlistt['tomoney'] = str(order.tomoney)
            orderlistt['trmoney'] = str(order.trmoney)
            orderlistt['amount'] = order.amount
            orderlistt['bank'] = order.bank
            orderlistt['dealtime'] = order.dealtime.strftime("%Y-%m-%d %H:%M:%S")
            goods = order.ordergoods_set.all()
            goodss = serializers.serialize("json", goods)
            orderlistt['goodss'] = goodss
            orderlists.append(orderlistt)
        return HttpResponse(json.dumps({"result": True, "list": orderlists}))


def cancel_order(request):
    if request.method == "GET":
        user = request.user
        orderid = request.GET.get("orderid","")
        Order.objects.filter(id=orderid, user=user).update(status=5)
        return HttpResponse(json.dumps({"result": True, "msg": "订单已取消"}))

