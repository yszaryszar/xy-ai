from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.register import register_routers

# 创建 FastAPI 应用实例
app = FastAPI(
    title="新语AI",  # 自定义标题
    description="AI辅助写作工具",  # 自定义描述
    version="1.0.0",  # API 版本
    openapi_url="/openapi.json",  # Swagger/OpenAPI JSON 路径
    docs_url="/docs",  # Swagger 文档路径
    redoc_url="/redoc",  # ReDoc 文档路径
)

# 配置 CORS（跨域资源共享）
origins = ["https://xyai.xin", "https://www.xyai.xin"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的源
    allow_credentials=True,  # 允许携带凭证
    allow_methods=["*"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的 HTTP 头
)

# 注册路由
register_routers(app)


# 定义根路径的处理函数
@app.get("/")
def read_root():
    return {"message": "Hello World!"}  # 返回 JSON 响应
