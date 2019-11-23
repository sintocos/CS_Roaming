# 计算机科学复杂性相关文章整理
1. 编程的本质是控制复杂性。  
Controlling complexity is the essence of computer programming. --Brian W. Kernighan  
2. 相比其他技术领域，美对于计算来说更为重要，因为软件超乎寻常的复杂，而美是对复杂性的一种终极防御。  
Beauty is more important in computing than anywhere else in technology because software is so complicated. Beauty is the ultimate defence against complexity. --David Gelernter  
3. 软件工程的目标是控制复杂度，而不是增加复杂性。  
The purpose of software engineering is to control complexity, not to create it.  --Dr. Pamela Zave  
4. 简单是可靠的先决条件。  
Simplicity is prerequisite for reliability.  --Edsger W. Dijkstra  
5. 可靠的最大敌人是复杂。  
The central enemy of reliability is complexity. --Geer et al.  
6. 有两种软件设计的方式：一种是使它足够简单以致于明显没有缺陷，另一种则是使它足够复杂以致于没有明显的缺陷。  
 There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies and the other way is to make it so complicated that there are no obvious deficiencies. --C.A.R. Hoare  
7. 计算机科学领域的任何问题都可以通过增加一个间接的中间层来解决。  
Any problem in computer science can be solved by another layer of indirection. --David Wheeler   

结构：  
1. More is different  
2. 可计算性和计算复杂性   
3. 复杂度控制--》软件工程，各个CS领域的控制复杂度的方法，编程思想，编程范式，编程原则，设计模式  
4. 复杂性科学，其他领域的复杂性系统，相关书籍和引用


## 1.More is different
###1.1 Less is more  
 如何正确理解Less is More: https://www.zhihu.com/question/33602031
###1.2 More is different  
 原文：https://www.tkm.kit.edu/downloads/TKM1_2011_more_is_different_PWA.pdf  
 知乎 https://www.zhihu.com/question/55213792  
  https://www.zhihu.com/question/26428553   
 涌现的数学基础：https://zhuanlan.zhihu.com/p/44095458  

###1.3 Comments  
评论https://www.nikhef.nl/~h02/more_is_different_comment.pdf  
https://journals.sagepub.com/doi/pdf/10.1068/b2702ed  
底层为01到上层宏大的架构，层层递进，层层抽象  
系统化 结构 组织 形式  
由more is different,转入CS复杂度  
少就是少，少既不比多好，也不比多差，少就是和多不一样  
还原论思想 整体大于局部 量变带来质变 形式决定功能  
计算机中，位置和元素，上下文决定元素的解释方式  

## 2.Computation Theory 
###2.1 可计算性  
  可计算性理论   wiki  
  微信：理论计算机科学浅涉：可计算性理论  
  微信：【CCCF专题】理论计算机  
###2.2 计算复杂性理论
  空间复杂度，时间复杂度  
###2.3 others  
许多学科都是人类知识的一种组织形式。  
CS重在对过程性知识的形式化，而数学重在对说明性知识的形式化。  

## 3.Complexity Control
###3.1 减少复杂度本身带来复杂度？ 复杂性如何度量? 复杂性带来什么问题  
  软件工程，人月神话  
  什么是好的软件或程序：可重用，健壮，可扩展，高内聚，低耦合...  
  关于软件本质的一点思考：https://www.cnblogs.com/aquastone/p/sicp-thinking.html  
  算法=逻辑+控制 程序=算法+数据结构 https://www.cnblogs.com/feng9exe/p/10186900.html  
  复杂性的随笔：https://www.cnblogs.com/feng9exe/category/1170468.html  
  程序的核心--复杂度： https://zhuanlan.zhihu.com/p/26887003   
###3.2 控制复杂度的基本思想：抽象  
  什么是抽象 https://juejin.im/entry/5a39bf776fb9a0450909a4d0  
  分层架构 https://juejin.im/entry/5b5a8928e51d4519115d2ab3  
  分层，分类，分治，封装....   分层太多间接太多降低效率，分层太少太复杂，是一个衡量的问题   
###3.3 各个CS领域中的复杂性和控制复杂性的手段  
  编码与信息论 大规模软件工程 缓存机制 数据结构（参考wiki）  
  计算机网络的分层设计，操作系统的三个抽象(CSAPP) 
  计算机科学的思考 https://blog.csdn.net/junecau/article/details/6963917  
###3.4 编程思想和编程方法
  什么是好的算法：参考清华大学邓俊辉的ppt  
  SOLID 等设计原则以及各种设计模式，编程范式 https://zhuanlan.zhihu.com/p/19736530  
  五大常用算法：分治，动态规划，贪心，回溯，分支界定 https://blog.csdn.net/qq_28598203/article/details/51914374  
  基础算法思想类别：递推 枚举 递归 分治 贪婪 回溯（试探） 模拟https://zhuanlan.zhihu.com/p/36903717  
  https://segmentfault.com/a/1190000014975027  

## 4.Complexity Science
   复杂性科学介绍，各个学科领域复杂系统的介绍,参考以下四本复杂性书籍  
   http://www.paper.edu.cn/scholar/showpdf/OUD2ANyIMTT0gxeQh

## 结语：
语言和词语也是对现实的一种抽象和简化，但有时反而更能反应本质，less is more.   
本文主要做的是一个整理的工作，也是在控制复杂度。  

## 推荐书籍和参考
1. 《复杂》https://book.douban.com/subject/6749832/ 
2. 《复杂性思考》https://book.douban.com/subject/24530461/ 
3. 《复杂性思想导论》https://book.douban.com/subject/3053195/ 
4. 《复杂性思维：物质、精神和人类的计算动力学》https://book.douban.com/subject/25847649/ 
5. 《计算机程序的构造和解释》SICP
6.  CSAPP
7.  Concepts Techniques and Models of Computer Programming
7.  冒号课堂
8.  计算机科学wiki https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6  

