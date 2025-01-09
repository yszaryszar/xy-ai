from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="新语AI",  # 自定义标题
    description="AI辅助写作工具",  # 自定义描述
    version="1.0.0",  # API 版本
    openapi_url="/openapi.json",  # Swagger/OpenAPI JSON 路径
    docs_url="/docs",  # Swagger 文档路径
    redoc_url="/redoc",
)

# 配置 CORS
origins = ["https://xyai.xin", "https://www.xyai.xin"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World!"}
