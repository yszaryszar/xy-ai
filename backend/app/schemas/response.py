#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 10:41
# @Author  : yszar
# @File    : response.py
# @Software: PyCharm
from typing import TypeVar, Generic

from pydantic import BaseModel, Field

T = TypeVar("T")


# 响应模式
class ResponseSchema(BaseModel, Generic[T]):
    code: int = Field(
        ..., description="状态码，例如：200 表示成功，400 表示客户端错误"
    )  # 状态码
    message: str = Field(
        ..., description="返回的状态信息，例如：'操作成功'"
    )  # 状态信息
    data: T = Field(
        ..., description="返回的数据内容，可能为任意数据结构"
    )  # 数据内容（可选）
