## 数据结构与算法 ##
1. 基本数据结构和算法
    - 排序：选择排序，冒泡排序，插入排序，希尔排序，归并排序，堆排序
    - 字符串：指纹，KMP，AC自动机，排序，Trie
    - 树：红黑树，B+树，LSM，AVL
    - 图：最短路径，最小生成树，拓扑排序，并查集，网络流
    - 散列表：拉链法，线性探测法
    - 其他：汉诺塔，哈夫曼编码
    - 基本算法思想：分治，动态规划，递归，贪心，回溯(试探)，枚举，递推，分支界定
2. 海量数据处理
     - TOP-K：局部淘汰，分治，Hash，最小堆
     - 海量数据判重
     - 海量数据排序
     - MapReduce
3. 数学逻辑
     - 概率题：抢红包，洗牌，蓄水池抽样，Rand7
     - 智力题


## 计算机组成原理 ##
1. 计算计的层次结构
     - 数字逻辑层
     - 微体系结构层
     - 指令系统层
     - 操作系统层
     - 汇编语言层
     - 并行体系结构
2. 基础知识
     - 硬件结构：冯诺依曼体系结构
     - 系统总线
     - 输入输出系统
     - 存储：寄存器，缓存，缓存一致性协议，DMA，异步同步
     - 计算机运算方法：原码，反码，补码，定点数，浮点数
     - 指令系统：指令的执行，数组/结构体/函数调用的实现
     - CPU结构和功能
     - 控制单元的功能
     - 控制单元的设计


## 操作系统 ##
1. 进程管理
    - 进程状态，进程线程协程，线程实现方式
    - 进程调度算法
    - 进程同步问题
    - 进程通信
    - 僵尸进程与孤儿进程：产生原因，区别，解决方法
    - 死锁：必要条件，解决策略
2. 内存管理
     - 虚拟内存
     - 页面置换算法：手写LRU
     - 分页与分段
3. 其他
     - 文件系统
     - 数据恢复原理
     - 静态链接与动态链接
     - 硬链接和软链接
     - 磁盘
     - 计算机存储体系
     - 网络处理
     - Linux常用命令：cat,find,grep,awk等


## 计算机网络 ##
1. TCP/IP
    - 体系结构
    - 网络协议图
    - 以太网
    - 网络硬件设备及其作用
    - 路由算法
    - IP协议：数据报，子网划分
    - TCP协议：TCP拥塞控制，与UDP区别
    - TCP连接：三次握手/四次挥手的过程和原因，TIME_WAIT
    - 可靠传输：TCP为何可靠，如何设计可靠的UDP协议
    - 其他协议：ARP，ICMP，DNS等
2. HTTP
     - GET/POST
     - 状态码
     - Cookie/Session
     - 连接管理
     - HTTP与FTP
     - HTTPs,HTTP/2,HTTP等版本比较
     - 缓存：Expires/Max-age区别和优先级
3. Socket
     - I/O模型：五种I/O模型
     - 多路复用：select/poll/epoll对比，各自的使用场景，epoll的水平触发和边缘触发
     - Java NIO


## 数据库 ##
1. 系统原理
     - ACID：Atomicity, Consistency, Isolation, Durability
     - 隔离级别：四大隔离级别，不可重复读和幻影读的原因
     - 封锁：封锁的类型和粒度，两阶段协议，隐式和显式锁定
     - 乐观锁与悲观锁
     - MVCC
     - 范式
     - SQL与NoSQL
2. SQL
    - 手写分组查询
    - 手写连接查询
    - 连接与子查询
    - drop/delete/truncate
    - 视图：概念和作用，何时能更新试图
    - 存储过程
    - 触发器
3. MySQL
     - B+ Tree
     - 索引以及优化
     - 查询优化
     - 水平切分和垂直切分
     - 主从复制
     - 日志
     - InnoDB与MyISAM
4. Redis
     - 使用场景
     - 与Memchached比较
     - 数据淘汰机制
     - 事件驱动模型
     - 集群与分布式
     - 事务
     - 线程安全问题
     - 字典和跳跃表
     - RDB和AOF持久化机制
     - 主从复制


## 面向对象 ##
1. 思想
     - 三大特性
     - 设计原则
2. 设计模式
     - 单例模式：手写单例模式，双重检验锁，静态内部类
     - 工厂模式：手写工厂模式
     - MVC：SpringMVC 
     - 代理模式：结合Spring中的AOP
     - JDK中常用的设计模式: 适配器，迭代器，装饰者


## 系统设计 ##
1. 基础
     - 性能：性能指标，性能优化
     - 伸缩性
     - 扩展性
     - 可用性：冗余，监控，服务降级
     - 安全性
2. 分布式
     - 分布式事务
     - CAP理论
     - BASE
     - 分布式锁
     - 分布式ID
     - Paxos/Raft
3. 集群
     - 负载均衡
     - Session管理
4. 缓存
     - 缓存特征
     - LRU
     - 缓存位置
     - CDN
     - 缓存问题
     - 一致性哈希
5. 攻击技术
     - XSS
     - CSRF
     - SQL注入
     - DDoS
6. 消息队列
     - 消息模型
     - 使用场景
     - 可靠性
7. 高并发系统
     - 秒杀系统
     - 限流算法
     - 服务熔断与服务降级
8. 服务拆分
     - 幂等性
     - 远程服务访问方法
     - 微服务/SOA
9. 实际中的系统设计
     - web页面请求过程
     - 二维码登录
     - TinyURL
     - KV存储系统
     - 搜索引擎


## 编程语言 ##
1. Java
     - Java基础：数据类型，String，运算，继承，Object通用方法，final与static，反射，异常，泛型
     - 容器：ArrayList/Vector/LinkedList/HashMap/ConcurrentHashMap源码分析
     - 并发：线程状态，使用线程，中断，互斥同步，线程之间协作，Java内存模型，线程安全，锁优化
     - Java虚拟机：运行时数据区域，垃圾搜集，内存分配与回收策略，类加载机制
     - I/O：磁盘操作，字节操作，字符操作，对象操作，网络操作，NIO
     - Web：Tomcat服务器，JSP/Servlet，Ajax，常用框架
2. Python
     - Python基础
     - 常用模块
     - 并发
     - Web开发
3. C++
     - C++基础
     - 面向对象编程
     - 容器
     - 模板与STL
4. JavaScript
     - JavaScript基础
     - 面向对象
     - DOM编程
     - Node.js
     - 框架


## 其他 ##
1. 中间件
     - RabbitMQ
     - ZooKeeper
     - Dubbo
     - Nginx
2. 工具
     - Git
     - Docker
     - 网络工具
     - 安全工具
     - 部署
     - 正则表达式
     - 构建工具：Maven
     - 常用框架：Spring，Django，PyTorch等
3. 代码
     - 代码可读性
     - 代码风格规范
     - 代码测试
     - 编程原则：先设计，模块化，反复推敲写优雅的代码，可读性与简单直观，考虑不重不漏
4. 编程范式
     - 面向过程
     - 面向对象
     - 命令式
     - 函数式
     - 声明式
     - 事件驱动
5. 面试
     - 简历
     - 内推/投递
     - 项目
     - 面试经验
     - 笔试常见题目
     - Leetcode/剑指Offer