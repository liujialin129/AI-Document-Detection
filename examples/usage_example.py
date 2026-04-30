"""
使用示例
展示如何使用智能文档分析 Agent 系统
"""

from src.agent import DocumentAnalysisAgent
from src.parser import DocumentParser


def example_basic_usage():
    """示例 1: 基本使用"""
    print("=" * 50)
    print("示例 1: 基本使用")
    print("=" * 50)
    
    # 初始化 Agent
    agent = DocumentAnalysisAgent()
    
    # 分析文档（需要替换为实际文件路径）
    # result = agent.analyze("example.pdf", task="总结文档要点")
    # print(result)
    
    print("代码示例已准备就绪")
    print("请配置 .env 文件中的 API Key 后运行")


def example_batch_processing():
    """示例 2: 批量处理"""
    print("=" * 50)
    print("示例 2: 批量处理")
    print("=" * 50)
    
    agent = DocumentAnalysisAgent()
    
    # 批量分析多个文档
    # documents = ["doc1.pdf", "doc2.docx", "doc3.xlsx"]
    # results = agent.batch_analyze(documents, task="提取关键信息")
    # 
    # for result in results:
    #     print(result)
    
    print("批量处理功能已准备就绪")


def example_document_parsing():
    """示例 3: 文档解析"""
    print("=" * 50)
    print("示例 3: 文档解析")
    print("=" * 50)
    
    parser = DocumentParser()
    
    # 支持多种格式
    formats = parser.get_supported_formats()
    print(f"支持的文档格式: {formats}")
    
    # 解析文档
    # content = parser.parse("example.pdf")
    # print(content[:500])  # 打印前 500 个字符
    
    print("文档解析功能已准备就绪")


def example_custom_task():
    """示例 4: 自定义任务"""
    print("=" * 50)
    print("示例 4: 自定义任务")
    print("=" * 50)
    
    agent = DocumentAnalysisAgent()
    
    # 自定义分析任务
    # tasks = [
    #     "提取所有日期和金额",
    #     "识别合同中的关键条款",
    #     "总结技术文档的核心要点",
    #     "对比两份文档的差异"
    # ]
    # 
    # for task in tasks:
    #     result = agent.analyze("document.pdf", task=task)
    #     print(f"任务: {task}")
    #     print(f"结果: {result['result']}\n")
    
    print("自定义任务功能已准备就绪")


def main():
    """主函数"""
    print("\n智能文档分析 Agent - 使用示例\n")
    
    # 运行示例
    example_basic_usage()
    print()
    
    example_batch_processing()
    print()
    
    example_document_parsing()
    print()
    
    example_custom_task()
    print()
    
    print("=" * 50)
    print("所有示例已展示完毕")
    print("=" * 50)
    print("\n下一步:")
    print("1. 复制 .env.example 为 .env")
    print("2. 配置你的 API Key")
    print("3. 准备测试文档")
    print("4. 运行示例代码的取消注释部分\n")


if __name__ == "__main__":
    main()
