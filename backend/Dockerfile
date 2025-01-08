# 使用 Python 构建后端服务
FROM python:3.13.1

WORKDIR /app

# 安装后端依赖
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# 启动 FastAPI 服务
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
