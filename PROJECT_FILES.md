# 项目文件清单

## 目录结构

```
mimo-project/
├── README.md                   # 项目说明文档
├── requirements.txt            # Python 依赖包
├── .env.example               # 环境变量示例
├── src/                       # 源代码目录
│   ├── agent.py               # 核心 Agent 实现
│   ├── parser.py              # 文档解析器
│   └── api.py                 # FastAPI 接口
├── examples/                  # 示例代码
│   └── usage_example.py       # 使用示例
├── docs/                      # 文档目录
│   ├── architecture.md        # 技术架构文档
│   └── mimo-application.md   # MiMo 申请说明
└── .gitignore                 # Git 忽略文件
```

## 文件说明

### 1. README.md
- 项目概述
- 核心痛点分析
- 技术架构说明
- 安装使用方法
- 应用场景介绍

### 2. requirements.txt
- 列出所有 Python 依赖包
- 包括 LangChain、FastAPI、文档处理库等

### 3. .env.example
- 环境变量配置示例
- 包括 API Key、模型配置等

### 4. src/agent.py
- DocumentAnalysisAgent 核心类
- 实现文档分析、批量处理等功能
- 集成 LangChain Agent

### 5. src/parser.py
- 多格式文档解析器
- 支持 PDF、DOCX、XLSX、TXT 等格式
- 使用策略模式设计

### 6. src/api.py
- FastAPI Web 服务
- 提供 RESTful API 接口
- 支持文件上传、批量分析等

### 7. examples/usage_example.py
- 代码示例
- 展示基本使用、批量处理、自定义任务等

### 8. docs/architecture.md
- 详细的技术架构文档
- 包括系统设计、核心逻辑流、扩展性设计等

## 快速开始

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置环境变量：
```bash
cp .env.example .env
# 编辑 .env 文件，配置 API Key
```

3. 运行示例：
```bash
python examples/usage_example.py
```

4. 启动 API 服务：
```bash
python src/api.py
```
