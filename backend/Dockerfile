# 使用 Python 3.13.1 基础镜像
FROM python:3.13.1-slim

# 设置工作目录
WORKDIR /backend

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 启动 FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
