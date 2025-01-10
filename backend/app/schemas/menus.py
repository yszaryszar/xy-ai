#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 12:55
# @Author  : yszar
# @File    : menus.py
# @Software: PyCharm

from typing import Optional

from pydantic import BaseModel, Field


# 菜单基础模型
class MenuBase(BaseModel):
    id: int = Field(..., title="菜单ID", description="菜单ID")  # 菜单ID
    parent_id: Optional[int] = Field(
        ..., title="父级菜单ID", description="父级菜单ID"
    )  # 父级菜单ID
    name: str = Field(..., title="菜单名称", description="菜单名称")  # 菜单名称
    url: str = Field(..., title="菜单URL", description="菜单URL")  # 菜单URL
    icon: str = Field(..., title="菜单图标", description="菜单图标")  # 菜单图标
    order: int = Field(
        ..., title="菜单排序", description="菜单排序,数字越小越靠前"
    )  # 菜单排序，数字越小越靠前
    children: list[dict] = Field(
        ..., title="子菜单", description="子菜单"
    )  # 子菜单列表
