#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 10:34
# @Author  : yszar
# @File    : response.py
# @Software: PyCharm
from typing import Any, Optional

from app.core.http_status import HttpStatus
from app.schemas.response import ResponseSchema


def success_response(data: Optional[Any] = None, message: str = "Success") -> dict:
    """
    返回成功响应的统一格式
    :param data: 返回的业务数据
    :param message: 返回的提示信息
    :return: 格式化响应
    """
    return ResponseSchema(
        code=HttpStatus.SUCCESS,  # 成功状态码
        message=message,  # 成功提示信息
        data=data,  # 返回的业务数据
    ).model_dump()


def error_response(code: int, message: str = "Error") -> dict:
    """
    返回错误响应的统一格式
    :param code: 错误状态码
    :param message: 错误提示信息
    :return: 格式化响应
    """
    return ResponseSchema(
        code=code,  # 错误状态码
        message=message,  # 错误提示信息
        data=None,  # 错误时无业务数据
    ).model_dump()


def paginated_response(
    data: list, total: int, page: int, size: int, message: str = "Success"
) -> dict:
    """
    返回分页响应的统一格式
    :param data: 当前页的数据
    :param total: 数据总数
    :param page: 当前页码
    :param size: 每页大小
    :param message: 提示信息
    :return: 格式化分页响应
    """
    return ResponseSchema(
        code=HttpStatus.SUCCESS,  # 成功状态码
        message=message,  # 成功提示信息
        data={
            "items": data,  # 当前页的数据
            "total": total,  # 数据总数
            "page": page,  # 当前页码
            "size": size,  # 每页大小
        },
    ).model_dump()
