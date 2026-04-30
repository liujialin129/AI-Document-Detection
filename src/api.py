"""
FastAPI Web 服务模块
提供 RESTful API 接口
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import tempfile
import os

from src.agent import DocumentAnalysisAgent

app = FastAPI(title="智能文档分析 Agent API")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化 Agent
agent = DocumentAnalysisAgent()


class AnalysisRequest(BaseModel):
    """分析请求模型"""
    task: str = "总结文档要点"
    document_path: Optional[str] = None


class BatchAnalysisRequest(BaseModel):
    """批量分析请求模型"""
    task: str = "总结文档要点"
    document_paths: List[str]


@app.get("/")
async def root():
    """API 根路径"""
    return {
        "name": "智能文档分析 Agent API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}


@app.post("/analyze")
async def analyze_document(request: AnalysisRequest):
    """分析单个文档
    
    Args:
        request: 分析请求
        
    Returns:
        分析结果
    """
    if not request.document_path:
        raise HTTPException(status_code=400, detail="缺少文档路径")
    
    try:
        result = agent.analyze(request.document_path, request.task)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze/upload")
async def analyze_uploaded_file(file: UploadFile = File(...), task: str = "总结文档要点"):
    """上传并分析文档
    
    Args:
        file: 上传的文件
        task: 分析任务
        
    Returns:
        分析结果
    """
    try:
        # 保存上传的文件
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file.filename.split('.')[-1]}") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name
        
        # 分析文档
        result = agent.analyze(tmp_path, task)
        
        # 清理临时文件
        os.unlink(tmp_path)
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/batch-analyze")
async def batch_analyze_documents(request: BatchAnalysisRequest):
    """批量分析文档
    
    Args:
        request: 批量分析请求
        
    Returns:
        分析结果列表
    """
    if not request.document_paths:
        raise HTTPException(status_code=400, detail="缺少文档路径列表")
    
    try:
        results = agent.batch_analyze(request.document_paths, request.task)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/supported-formats")
async def get_supported_formats():
    """获取支持的文档格式"""
    from src.parser import DocumentParser
    parser = DocumentParser()
    return {"formats": parser.get_supported_formats()}


def start_server(host: str = "0.0.0.0", port: int = 8000):
    """启动 API 服务
    
    Args:
        host: 主机地址
        port: 端口号
    """
    import uvicorn
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
