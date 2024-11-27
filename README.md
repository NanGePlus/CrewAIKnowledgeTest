# 0、CrewAI相关项目视频                
**(1)FastAPI+CrewAI+MySQL+Celery实现AI Agent复杂工作流，支持工作流的并发异步调度和全生命周期状态监测，支持gpt、国产、本地大模型**                                             
https://www.bilibili.com/video/BV1P91tY6ELE/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                             
https://youtu.be/G-Sa5OcuQRE           
**(2)详细剖析源码帮助你快速构建自己的工作流，FastAPI+CrewAI+MySQL+Celery实现AI Agent复杂工作流，支持gpt、国产、本地大模型**                      
https://www.bilibili.com/video/BV1nk17YMEec/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                    
https://youtu.be/U_Af8HGw1Hk              

# 1、项目介绍
## 1.1、本次分享介绍
CrewAI新版本支持使用Knowledge属性将txt、PDF、CSV、Excel、JSON等多种数据格式内容及多文件混合作为知识增强知识库提供给Crew中的Agent使用                      
**本次分享的测试用例如下:**                               
(1)单个短字符串创建知识库              
(2)单个长字符串创建知识库                   
(3)多个短字符串创建知识库                                                
(4)多个长字符串创建知识库              
(5)单个短文本文件创建知识库                 
(6)单个长文本文件创建知识库                   
(7)多个短文本文件创建知识库                  
(8)多个长文本文件创建知识库                  
(9)混合型创建知识库                    
(10)PDF文件创建知识库                     
(11)CSV文件创建知识库                   
(12)JSON文件创建知识库                     
(13)excel文件创建知识库                 

## 1.2 CrewAI介绍
### (1)简介    
CrewAI是一个用于构建多Agent协作应用的框架，它能够让多个具有不同角色和目标的Agent共同协作，完成复杂的任务                          
该工具可以将任务分解，分配给不同的Agent，借助它们的特定技能和工具，完成各自负责的子任务，最终实现整体任务目标              
官网:https://www.crewai.com/                                          
GitHub:https://github.com/crewAIInc/crewAI                                           
### (2)核心概念
**(1)Agents**          
是一个自主可控单元，通过编程可以实现执行任务、作出决定、与其他Agent协作交流，可类比为团队中的一员，拥有特定的技能和任务                                        
role(角色):定义Agent在团队中的角色                                          
goal(目标):定义Agent需要实现的目标                             
backstory(背景信息):定义Agent的背景描述信息                                              
**(2)Tasks**               
分配给Agent的具体任务，并定义任务所需的所有细节                                               
description(任务描述):简明扼要说明任务要求                                                 
agent(分配的Agent):分配负责该任务的Agent                                                
expected_output(期望输出):期望任务完成后输出的详细描述                                                         
Tools(工具列表):为Agent提供可用于执行该任务的工具列表                   
output_json(输出json):设置任务的输出为自定义的json数据格式                                
output_file(输出到文件):将任务结果输出到一个文件中，指定输出的文件格式                                                     
callback(回调函数):指定任务执行完成后的回调处理函数                                                 
**(3)Processes**                      
CrewAI中负责协调Agent执行任务,类似于团队中的项目经理,确保任务分配和执行效率与预定计划保持一致                       
目前拥有两种运行机制:                             
sequential(按顺序运行):以深思熟虑、系统化的方式推进各项任务，按照任务列表中预定义的顺序执行，一个任务的输出作为下一个任务的上下文                               
hierarchical(按顶层规划运行):允许指定一个自定义的管理角色的Agent，负责监督任务执行，包括计划、授权和验证。任务不是预先分配的，而是根据Agent的能力进行任务分配，审查产出并评估任务完成情况                          
**(4)Crews**          
1个crew代表一个协作团队，即一组协作完成一系列任务的Agent                            
Agents(Agent列表):分配给crew的Agents                                   
Tasks(任务列表):分配给crew的Tasks                                                
Process(运行机制):sequential(按顺序运行)、hierarchical(按顶层规划运行)                                                 
manager_llm(大模型):在Process为hierarchical下指定的大模型                                    
**(5)Flows**          
为构建复杂的AI Agent WorkFlow(工作流)设计的一个强大的技术框架                 
**核心特点:**           
(a)简化工作流程创建                      
轻松串联多个crew和任务(自定义的方法)，创建复杂的工作流              
(b)状态管理                  
Flows可以在工作流中的不同任务之间轻松管理和共享状态              
(c)事件驱动架构                                         
基于事件驱动模型构建可实现动态响应的工作流           
(d)灵活的控制流                 
在工作流中实现条件逻辑、循环、分支等逻辑控制                   
**关键参数:**            
(a)@start()装饰器                               
用于将一个方法标记为Flow的起点。在一个Flow中支持对多个方法进行@start()标记，当Flow启动时，所有用@start()装饰的方法都会并行执行           
(b)@listen装饰器                                    
用于将一个方法标记为Flow中的监听器。在一个Flow中支持对多个方法进行@listen()装饰，当Flow启动后被监听的方法执行完成后，所有用@listen()监听该方法的方法都会被执行             
(c)@router装饰器                                                         
在Flow中允许根据方法的输出内容来定义路由的执行逻辑，根据方法的输出指定不同的路由，从而动态控制执行流程                     
**条件控制:**              
(a)条件逻辑 or_()                             
Flows中@listen()中可以使用or_()函数允许监听多个方法，在这些被监听方法中任何一个执行完成后，监听该方法的方法就会被执行               
(b)条件逻辑 and_()                                           
Flows中@listen()中可以使用and_()函数允许监听多个方法，在这些被监听方法中全部执行完成后，监听该方法的方法就会被执                 
**结果输出:**                 
(a)检索结果的最后输出                              
运行Flow时，最终的输出是由最后完成的方法决定的                                 
(b)访问和更新状态                                  
状态可用于在Flow中的不同方法之间存储和共享数据                       
(c)状态管理                  
有效管理状态对于构建可靠、可维护的AI工作流至关重要。 Flows为非结构化、结构化状态管理提供了强大的机制，允许根据需求自行选择            
非结构化状态管理:所有状态都存储在Flow类的状态属性中。这种方法具有很大的灵活性，开发人员可随时添加或修改状态属性，而无需定义严格的模式            
结构化状态管理:利用预定义的模式来确保整个工作流程的一致性和类型安全性                      
**(6)Knowledge**          
使用Knowledge属性支持将txt、PDF、CSV、Excel、JSON等多种数据格式内容及多文件混合作为知识增强知识库提供给Crew中的Agent使用         


# 2、前期准备工作
## 2.1 开发环境搭建:anaconda、pycharm
anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可                                      
pycharm:提供集成开发环境，官网下载社区版本安装包安装即可                                               
可参考如下视频进行安装，【大模型应用开发基础】集成开发环境搭建Anaconda+PyCharm                                                          
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                             
https://youtu.be/myVgyitFzrA          

## 2.2 大模型相关配置
(1)GPT大模型使用方案              
(2)非GPT大模型(国产大模型)使用方案(OneAPI安装、部署、创建渠道和令牌)                 
(3)本地开源大模型使用方案(Ollama安装、启动、下载大模型)                         
可参考如下视频:                         
提供一种LLM集成解决方案，一份代码支持快速同时支持gpt大模型、国产大模型(通义千问、文心一言、百度千帆、讯飞星火等)、本地开源大模型(Ollama)                       
https://www.bilibili.com/video/BV12PCmYZEDt/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                 
https://youtu.be/CgZsdK43tcY             


# 3、项目初始化
## 3.1 下载源码
GitHub或Gitee中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/CrewAIKnowledgeTest                                                                  
https://gitee.com/NanGePlus/CrewAIKnowledgeTest                                                                  

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境                    
项目名称：CrewAIKnowledgeTest                                      

## 3.3 将相关代码拷贝到项目工程中             
直接将下载的文件夹中的文件拷贝到新建的项目目录中                 

## 3.4 安装项目依赖          
打开命令行终端在项目根目录下执行如下命令安装依赖包                                            
pip install -r requirements.txt                     
每个软件包后面都指定了本次视频测试中固定的版本号            
**注意:** 截止2024.11.27，本项目crewai最新版本0.83.0，建议先使用要求的对应版本进行本项目测试，避免因版本升级造成的代码不兼容。测试通过后，可进行升级测试。          


# 4、项目测试          
运行 python knowledge.py 脚本测试                    
运行脚本前，请根据自己实际情况配置如下参数                                   
os.environ["OPENAI_API_BASE"] = "https://api.wlai.vip/v1"                 
os.environ["OPENAI_API_KEY"] = "sk-dUWW1jzueJ4lrDixWaPsq7nnyN5bCucMzvldpNJwfJlIvAcC"                     
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"                   







