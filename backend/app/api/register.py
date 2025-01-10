#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 11:59
# @Author  : yszar
# @File    : register.py
# @Software: PyCharm
from app.api.v1 import menus


def register_routers(app):
    # 注册 V1 路由
    app.include_router(menus.router, prefix="/v1/menus", tags=["pages"])
