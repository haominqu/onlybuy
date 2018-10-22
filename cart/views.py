from django.shortcuts import render
from .models import *
from memberapp import *
from django.db import DatabaseError
from django.http import request, response, HttpResponse
import logging
import json
from django.core import serializers
# Create your views here.


def add_cart(request):
    if request.method == "POST":
        user = request.user
        goodsid = request.POST.get("goodsid", "")
        amount = request.POST.get("amount", "")
        new_cart = Cart()
        try:
            goods = GoodsDetail.objects.get(id=goodsid)
        except DatabaseError as e:
            logging.warnning(e)
        oldcart = Cart.objects.filter(user_id=user.id, goods_id=goodsid)
        if oldcart:
            oldcart[0].amount = oldcart[0].amount + amount
            oldcart[0].save()
        else:
            new_cart.user = user
            new_cart.goods = goods
            new_cart.amount = int(amount)
            new_cart.save()
        return HttpResponse(json.dumps({'result':"添加成功"}))
    elif request.method == "GET":
        pass


def delete_cart(request):
    if request.method == "GET":
        user = request.user
        cartid = request.GET.get("cartid", "")
        try:
            delcart = Cart.objects.filter(user_id=user.id, id=cartid)
            delcart.delete()
        except BaseException as e:
            logging.warning(e)
        return HttpResponse(json.dumps({"result":"删除成功"}))


def change_cart(request):
    if request.method == "GET":
        user = request.user
        cartid = request.GET.get("cartid", "")
        single = request.GET.get("single", "")
        try:
            delcart = Cart.objects.filter(user_id=user.id, id=cartid)
            if single == 0:
                delcart[0].amount = delcart[0].amount+1
            elif single == 1:
                delcart[0].amount = delcart[0].amount-1
                if delcart[0].amount <= 0:
                    delcart.delete()
            delcart[0].save()
        except BaseException as e:
            logging.warning(e)
        return HttpResponse(json.dumps({"result":"删除成功"}))


def cart_list(request):
    if request.method == "GET":
        user = request.user
        find_carts = Cart.objects.filter(user_id=user.id)
        find_carts = serializers.serialize("json", find_carts)
        return HttpResponse(json.dumps({"cartlist":find_carts}))


def add_favorite(request):
    if request.method == "GET":
        user = request.user
        goodsid = request.GET.get("goodsid", "")
        goods = Goods.objects.get(id=goodsid)
        favorite = Favorite.objects.filter(goods_id=goodsid)
        if favorite:
            return HttpResponse(json.dumps({"result": "已添加"}))
        else:
            Favorite.objects.create(user=user,goods=goods)
            return HttpResponse(json.dumps({"result": "已添加"}))


def delete_favorite(request):
    if request.method == "POST":
        user = request.user
        fids = request.POST.get("fids","")
        for fid in fids:
            Favorite.objects.filter(id=fid).delete()
        return HttpResponse(json.dumps({"result": "已删除"}))
