#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 11:07
# @Author  : yszar
# @File    : http_status.py
# @Software: PyCharm
class HttpStatus:
    SUCCESS = 200  # 成功
    CREATED = 201  # 创建成功
    NO_CONTENT = 204  # 无内容
    BAD_REQUEST = 400  # 错误请求
    UNAUTHORIZED = 401  # 未授权
    FORBIDDEN = 403  # 禁止访问
    NOT_FOUND = 404  # 未找到
    METHOD_NOT_ALLOWED = 405  # 方法不允许
    CONFLICT = 409  # 冲突
    INTERNAL_SERVER_ERROR = 500  # 服务器内部错误
