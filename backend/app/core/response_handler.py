#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/10 11:08
# @Author  : yszar
# @File    : response_handler.py
# @Software: PyCharm
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from app.core.http_status import HttpStatus
from app.schemas.response import ResponseSchema


# 异步响应处理器
async def response_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        # 处理标准化的 JSON 响应
        if response.status_code == HttpStatus.SUCCESS:
            return JSONResponse(
                status_code=response.status_code,
                content=ResponseSchema(
                    code=response.status_code,
                    message="Success",  # 成功消息
                    data=response.body,  # 响应数据
                ).dict(),
            )
        return response
    except HTTPException as exc:
        # 捕获 HTTP 异常并标准化响应
        return JSONResponse(
            status_code=exc.status_code,
            content=ResponseSchema(code=exc.status_code, message=exc.detail).dict(),
        )
    except Exception as exc:
        # 捕获未知异常
        return JSONResponse(
            status_code=HttpStatus.INTERNAL_SERVER_ERROR,
            content=ResponseSchema(
                code=HttpStatus.INTERNAL_SERVER_ERROR, message=str(exc)  # 异常消息
            ).dict(),
        )
