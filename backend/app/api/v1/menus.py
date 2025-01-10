#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 09:09
# @Author  : yszar
# @File    : menus.py
# @Software: PyCharm
from typing import List

from fastapi import APIRouter

from app.core.http_status import HttpStatus
from app.crud.menus import get_menu
from app.schemas.menus import MenuBase
from app.schemas.response import ResponseSchema
from app.utils.response import success_response, error_response

router = APIRouter()


@router.get(
    "/",
    response_model=ResponseSchema[List[MenuBase]],
    summary="获取所有菜单",
    description="获取所有菜单",
)
async def read_menu():
    """获取所有菜单"""
    menus = get_menu()
    if not menus:
        return error_response(code=HttpStatus.SUCCESS, message="Menus not found")
    formatted_menus = [MenuBase(**menu) for menu in menus]
    return success_response(data=formatted_menus, message="Get menus successfully")
