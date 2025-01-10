#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 12:40
# @Author  : yszar
# @File    : menus.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)  # 菜单 ID，主键
    parent_id = Column(Integer, ForeignKey("menu.id"), nullable=True)  # 父菜单 ID，外键
    name = Column(String, nullable=False)  # 菜单名称
    url = Column(String, nullable=True)  # 菜单 URL
    icon = Column(String, nullable=True)  # 菜单图标
    order = Column(Integer, nullable=False)  # 菜单顺序

    def __repr__(self):
        # 返回菜单对象的字符串表示
        return f"<Menu(id={self.id}, name={self.name}, url={self.url}, icon={self.icon}, order={self.order})>"
