"""
智能文档分析 Agent 核心模块
"""

from langchain_openai import ChatOpenAI
from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from typing import Dict, List, Any
import os
from dotenv import load_dotenv

load_dotenv()


class DocumentAnalysisAgent:
    """文档分析 Agent 主类"""
    
    def __init__(self, model_name: str = None, temperature: float = 0.7):
        """初始化 Agent
        
        Args:
            model_name: 模型名称，默认从环境变量读取
            temperature: 温度参数
        """
        self.model_name = model_name or os.getenv("MODEL_NAME", "gpt-4-turbo-preview")
        self.temperature = temperature
        
        # 初始化 LLM
        self.llm = ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL")
        )
        
        # 初始化记忆
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # 创建 Agent
        self.agent_executor = self._create_agent()
    
    def _create_agent(self) -> AgentExecutor:
        """创建 Agent 执行器"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是一个专业的文档分析助手。
            
你的能力包括：
1. 提取文档中的关键信息
2. 总结文档要点
3. 回答基于文档的问题
4. 分析文档结构和内容
5. 对比多个文档的异同

请根据用户的需求，选择合适的工具完成任务。"""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        agent = create_structured_chat_agent(
            llm=self.llm,
            prompt=prompt,
            tools=[]  # 这里可以添加工具
        )
        
        return AgentExecutor(
            agent=agent,
            tools=[],
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True
        )
    
    def analyze(self, document_path: str, task: str = "总结文档") -> Dict[str, Any]:
        """分析文档
        
        Args:
            document_path: 文档路径
            task: 分析任务描述
            
        Returns:
            分析结果字典
        """
        # 读取文档内容
        from src.parser import DocumentParser
        parser = DocumentParser()
        content = parser.parse(document_path)
        
        # 构建分析提示
        prompt = f"""
文档内容：
{content[:4000]}  # 限制长度

任务：{task}

请提供详细的分析结果。
"""
        
        # 执行分析
        result = self.agent_executor.invoke({"input": prompt})
        
        return {
            "status": "success",
            "task": task,
            "result": result.get("output", ""),
            "document_path": document_path
        }
    
    def batch_analyze(self, document_paths: List[str], task: str) -> List[Dict[str, Any]]:
        """批量分析文档
        
        Args:
            document_paths: 文档路径列表
            task: 分析任务描述
            
        Returns:
            分析结果列表
        """
        results = []
        for path in document_paths:
            try:
                result = self.analyze(path, task)
                results.append(result)
            except Exception as e:
                results.append({
                    "status": "error",
                    "document_path": path,
                    "error": str(e)
                })
        
        return results
