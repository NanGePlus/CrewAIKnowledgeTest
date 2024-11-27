import os
from pathlib import Path
from crewai import Agent, Task, Crew, Process
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource



# 设置大模型相关参数
os.environ["OPENAI_API_BASE"] = "https://api.wlai.vip/v1"
os.environ["OPENAI_API_KEY"] = "sk-dUWW1jzueJ4lrDixWaPsq7nnyN5bCucMzvldpNJwfJlIvAcC"
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"



# 1、单个短字符串创建知识库
def test_single_short_string():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store001")

    content = "南哥最喜欢的B站频道是南哥AGI研习社。"
    string_source = StringKnowledgeSource(
        content=content, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [string_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 2、单个长字符串创建知识库
def test_single_2k_character_string():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store002")

    content = (
        "南哥是一名软件工程师，现居旧金山。"
        "他喜欢徒步旅行，经常去湾区的小径。"
        "南哥有一只宠物狗，名叫 “麦克斯”，是一只金毛猎犬。"
        "他喜欢阅读科幻小说，最喜欢的作家是艾萨克-阿西莫夫。"
        "南哥最喜欢的电影是《盗梦空间》，他喜欢和朋友一起看这部电影。"
        "他还喜欢墨西哥美食，尤其是玉米饼和卷饼。"
        "南哥会弹吉他，经常在当地的露天麦克风之夜表演。"
        "他正在学习法语，计划明年访问巴黎。"
        "南哥对技术充满热情，经常参加城市里的技术聚会。"
        "他对人工智能和机器学习也很感兴趣，目前正在研究一个与自然语言处理相关的项目。"
        "南哥最喜欢的颜色是蓝色，他经常穿蓝色衬衫。"
        "他喜欢烹饪，经常在周末尝试新菜谱。"
        "南哥是个早起的人，他喜欢在公园跑步来开始新的一天。"
        "他也是一个咖啡爱好者，喜欢尝试不同的咖啡混合物。"
        "南哥是当地一个读书俱乐部的成员，喜欢与其他成员讨论书籍。"
        "他还是桌游爱好者，经常在家里举办游戏之夜。"
        "南哥是环境保护的倡导者，是当地清洁活动的志愿者。"
        "他还是有抱负的软件开发人员的导师，喜欢与他人分享自己的知识。"
        "南哥最喜欢的运动是篮球，他经常在周末和朋友们一起打篮球。"
        "他还是金州勇士队的球迷，喜欢观看他们的比赛。"
    )
    string_source = StringKnowledgeSource(
        content=content, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [string_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥最喜欢的电影是什么?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 3、多个短字符串创建知识库
def test_multiple_short_strings():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store003")

    contents = [
        "南哥喜欢徒步旅行。",
        "南哥有一只猫叫微微。",
        "南哥喜欢python语言。",
    ]

    string_sources = [
        StringKnowledgeSource(content=content, metadata={"preference": "personal"})
        for content in contents
    ]

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": string_sources,
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥的宠物是什么?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 4、多个长字符串创建知识库
def test_multiple_2k_character_strings():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store004")

    contents = [
        (
            "南哥是一名软件工程师，现居旧金山。"
            "他喜欢徒步旅行，经常去湾区的小径。"
            "南哥有一只宠物狗，名叫 “麦克斯”，是一只金毛猎犬。"
            "他喜欢阅读科幻小说，最喜欢的作家是艾萨克-阿西莫夫。"
            "南哥最喜欢的电影是《盗梦空间》，他喜欢和朋友一起看这部电影。"
            "他还喜欢墨西哥美食，尤其是玉米饼和卷饼。"
            "南哥会弹吉他，经常在当地的露天麦克风之夜表演。"
            "他正在学习法语，计划明年访问巴黎。"
            "南哥对技术充满热情，经常参加城市里的技术聚会。"
            "他对人工智能和机器学习也很感兴趣，目前正在研究一个与自然语言处理相关的项目。"
            "南哥最喜欢的颜色是蓝色，他经常穿蓝色衬衫。"
            "他喜欢烹饪，经常在周末尝试新菜谱。"
            "南哥是个早起的人，他喜欢在公园跑步来开始新的一天。"
            "他也是一个咖啡爱好者，喜欢尝试不同的咖啡混合物。"
            "南哥是当地一个读书俱乐部的成员，喜欢与其他成员讨论书籍。"
            "他还是桌游爱好者，经常在家里举办游戏之夜。"
            "南哥是环境保护的倡导者，是当地清洁活动的志愿者。"
            "他还是有抱负的软件开发人员的导师，喜欢与他人分享自己的知识。"
            "南哥最喜欢的运动是篮球，他经常在周末和朋友们一起打篮球。"
            "他还是金州勇士队的球迷，喜欢观看他们的比赛。"
        ) * 2,
        (
            "南哥热爱旅行，已经去过 20 多个国家。"
            "他能说一口流利的西班牙语，经常和朋友们一起练习。"
            "南哥最喜欢的城市是巴塞罗那，他喜欢那里的建筑和文化。"
            "他是一个美食家，喜欢尝试新的美食，尤其喜欢寿司。"
            "南哥是一名狂热的自行车爱好者，经常参加当地的自行车赛事。"
            "他还是一名摄影师，喜欢拍摄风景和城市景观。"
            "南哥是一名技术爱好者，关注小工具和软件的最新趋势。"
            "他也是虚拟现实的爱好者，拥有一个 VR 头盔。"
            "南哥最喜欢的一本书是《银河系漫游指南》。"
            "他喜欢看纪录片，学习历史和科学知识。"
            "南哥喜欢喝咖啡，他收藏了来自不同国家的咖啡杯。"
            "他还是爵士乐迷，经常参加现场表演。"
            "南哥是当地一家跑步俱乐部的成员，经常参加马拉松比赛。"
            "他还是当地一家动物收容所的志愿者，帮助遛狗。"
            "南哥最喜欢的节日是圣诞节，他喜欢装饰自己的家。"
            "他还是一个经典电影迷，收藏了很多 DVD。"
            "他还是一个谜题迷，闲暇时喜欢解谜。"
            "南哥最喜欢的运动是足球，他经常和朋友一起踢球。"
            "他还是巴塞罗那足球俱乐部的球迷，喜欢观看他们的比赛。"
        ) * 2,
    ]

    string_sources = [
        StringKnowledgeSource(content=content, metadata={"preference": "personal"})
        for content in contents
    ]

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": string_sources,
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥最喜欢的一本书是什么?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 5、单个短文本文件创建知识库
def test_single_short_file():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store005")

    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定到文件路径
    file_path = current_dir / "files/short_file.txt"

    file_source = TextFileKnowledgeSource(
        file_path=file_path, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [file_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥最喜欢的美食是什么?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 6、单个长文本文件创建知识库
def test_single_2k_character_file():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store006")

    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定到文件路径
    file_path = current_dir / "files/long_file.txt"

    file_source = TextFileKnowledgeSource(
        file_path=file_path, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [file_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥最喜欢的电影是什么?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 7、多个短文本文件创建知识库
def test_multiple_short_files():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store007")

    # 初始化文件路径列表
    file_paths = []
    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定文件目录
    files_dir = current_dir / "files/short_files"

    # 遍历文件目录中所有符合格式的文件
    for file_path in files_dir.glob("file_*.txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if "工作" in content:
                metadata = {"category": "profession", "source": "occupation"}
            elif "生活" in content:
                metadata = {"category": "city", "source": "personal"}
            elif "美食" in content:
                metadata = {"category": "hobby", "source": "personal"}
            else:
                metadata = {"preference": "personal"}
        file_paths.append((file_path, metadata))

    file_sources = [
        TextFileKnowledgeSource(file_path=path, metadata=metadata)
        for path, metadata in file_paths
    ]

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": file_sources,
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥的工作是什么?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 8、多个长文本文件创建知识库
def test_multiple_2k_character_files():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store008")

    # 初始化文件路径列表
    file_paths = []
    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定文件目录
    files_dir = current_dir / "files/long_files"

    # 遍历文件目录中所有符合格式的文件
    for file_path in files_dir.glob("file_*.txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            metadata = {"preference": "personal"}
        file_paths.append((file_path, metadata))

    file_sources = [
        TextFileKnowledgeSource(file_path=path, metadata=metadata)
        for path, metadata in file_paths
    ]

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": file_sources,
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥最喜欢的电影是什么?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 9、混合型创建知识库
def test_hybrid_string_and_files():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store009")

    string_contents = [
        "南哥喜欢徒步旅行。",
        "南哥有一只猫叫微微。",
        "南哥喜欢的编程语言是python。",
    ]
    string_sources = [
        StringKnowledgeSource(content=content, metadata={"preference": "personal"})
        for content in string_contents
    ]

    # 初始化文件路径列表
    file_paths = []
    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定文件目录
    files_dir = current_dir / "files/short_files"
    for file_path in files_dir.glob("file_*.txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if "工作" in content:
                metadata = {"category": "profession", "source": "occupation"}
            elif "生活" in content:
                metadata = {"category": "city", "source": "personal"}
            elif "美食" in content:
                metadata = {"category": "hobby", "source": "personal"}
            else:
                metadata = {"preference": "personal"}
        file_paths.append((file_path, metadata))

    file_sources = [
        TextFileKnowledgeSource(file_path=path, metadata=metadata)
        for path, metadata in file_paths
    ]

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": string_sources + file_sources,
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥最喜欢的编程语言是什么?"})
    # crew.kickoff(inputs={"question": "南哥生活在哪里?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 10、PDF文件创建知识库
def test_pdf_knowledge_source():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store010")

    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定到文件路径
    pdf_path = current_dir / "files/data.pdf"

    pdf_source = PDFKnowledgeSource(
        file_path=pdf_path, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解文档的一切。",
        backstory="""你是一个回答文档内容的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [pdf_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "张三九的基本信息?"})


# 11、CSV文件创建知识库
def test_csv_knowledge_source():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store011")

    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定到文件路径
    csv_path = current_dir / "files/data.csv"

    csv_source = CSVKnowledgeSource(
        file_path=csv_path, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [csv_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥住在哪里?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 12、JSON文件创建知识库
def test_json_knowledge_source():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store012")

    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定到文件路径
    json_path = current_dir / "files/data.json"

    json_source = JSONKnowledgeSource(
        file_path=json_path, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [json_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥住在哪里?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})


# 13、excel文件创建知识库
def test_excel_knowledge_source():
    # 指定向量数据库持久化文件夹
    os.environ["CREWAI_STORAGE_DIR"] = ("vector_store013")

    # 获取当前位置路径
    current_dir = Path(__file__).parent
    # 指定到文件路径
    excel_path = current_dir / "files/data.xlsx"

    excel_source = ExcelKnowledgeSource(
        file_path=excel_path, metadata={"preference": "personal"}
    )

    agent = Agent(
        role="About User",
        goal="你了解用户的一切。",
        backstory="""你是了解用户及用户喜好的高手。""",
        verbose=True
    )

    task = Task(
        description="回答有关用户的问题: {question}",
        expected_output="解答问题。",
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge={
            "sources": [excel_source],
            "metadata": {"preference": "personal"},
            "embedder_config": {
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"}
            }
        }
    )

    crew.kickoff(inputs={"question": "南哥住在哪里?"})
    # crew.kickoff(inputs={"question": "南哥最喜欢的B站频道是什么?"})



if __name__ == '__main__':
    test_single_short_string()
    # test_single_2k_character_string()
    # test_multiple_short_strings()
    # test_multiple_2k_character_strings()
    # test_single_short_file()
    # test_single_2k_character_file()
    # test_multiple_short_files()
    # test_multiple_2k_character_files()
    # test_hybrid_string_and_files()
    # test_csv_knowledge_source()
    # test_json_knowledge_source()
    # test_excel_knowledge_source()
    # test_pdf_knowledge_source()
