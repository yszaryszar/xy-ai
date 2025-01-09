#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/9 16:12
# @Author  : yszar
# @File    : config.py
# @Software: PyCharm
from pydantic import BaseSettings


class Settings(BaseSettings):
    mysql_host: str
    mysql_port: int
    mysql_user: str
    mysql_password: str
    mysql_db: str

    class Config:
        env_file = ".env"  # 从 .env 文件加载配置


settings = Settings()
