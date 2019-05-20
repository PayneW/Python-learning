## Learning-Python
 Python 学习

- [Google Python 风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/)

- 常用 Linux 命令的基本使用

    | 序号 | 命令 | 对应英文 | 作用 |
    |:----:|:----:|:----:|:----:|
    | 01 | ls | list | 查看当前文件夹下的内容 |
    | 02 | pwd | print work directory(打印工作目录) | 查看当前所在文件夹 |
    | 03 | cd [目录名] | change directory | 切换文件夹 |
    | 04 | touch [文件名] | touch | 如果文件不存在，新建文件 |
    | 05 | mkdir [目录名] | make directory | 创面目录 |
    | 06 | rm [文件名] | remove | 删除指定的文件名 |
    | 07 | clear | clear | 清屏 |

- 在终端中放大/缩小字体:
    + 放大: `ctrl + shift + =`
    + 缩小: `ctrl + -`

- DSL: Domain Specific Language 的缩写，翻译成中文就是 "特定领域语言"。(例如: html, css, SQL...)
- GPPL: General Purpose Programming Language 即 "通用目标语言"。(例如: C++, Java, Python, JavaScript...)



- Python 注释: 
    + """docstring 文档注释"""
    + ``` # 单行注释 ```

## [一文看懂 Python 面向对象编程 (Python 学习与新手入门必看)](https://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483689&idx=1&sn=3c6e345f0dc083450a034a292abcdcba&chksm=a73c6111904be8070fda0c5e64f9263193936aa9e80da13f0f8d77ad6559b431b4d576c0095c&scene=21#wechat_redirect)





- 人类的大脑是如何学习到知识的？答案是通过不断的思考。在不断地学习和思考的过程中，人的大脑内部产生着剧烈的神经活动，迫使脑神经之间建立了更多的连接。随着神经元之间连接越来越多，我们对问题的认识也就越来越深刻，遇到类似问题反应也会越来越快。不仅如此，甚至还能触类旁通，举一反三，乃至和其他的领域结合，产生创新性的想法。这表现出来，就是你更聪明了。
    + [作者：liuyubobobo](https://www.imooc.com/article/44792)




## Python Philosophy（Python哲学）翻译及简析
[来源](http://oldratlee.com/147/tech/python/python-philosophy.html)
1. Beautiful is better than ugly.
   美优于丑。
1. Explicit is better than implicit.
   直白优于隐晦。
1. Simple is better than complex 【1】.
   简单优于复杂。
1. Complex is better than complicated 【2】.
   复杂优于纠结。
1. Flat is better than nested.
   扁平优于嵌套。
1. Sparse is better than dense 【3】.
   稀疏优于稠密。
1. Readability counts.
   可读性有重要意义的。
1. Special cases aren’t special enough to break the rules.
   特例可以，但不能特例到打破规则。
   + Although practicality beats purity.
     尽管我们在纯粹性和实用性之间是倾向实用性的。
1. Errors should never pass silently.
    出错决不允许静静地Pass。
   + Unless explicitly silenced.
     除非明确的说明了是静静地Pass。
1. In the face of ambiguity, refuse the temptation to guess.
   面对二义性情况时，要拒绝任何猜的诱惑。
1. There should be one– and preferably only one –obvious way to do it.
   显而易见的做法应该是一个，并且宁愿只有一个。
1. Although that way may not be obvious at first unless you’re Dutch 【4】.
   尽管这个做法可能刚开始的时候不是那么显而易见的，毕竟你不是荷兰人Python之父。
1. Now is better than never.
    “现在” 优于 “决不”。
    + Although never is often better than right now.
      尽管 “决不” 常常优于 “马上”。
1. If the implementation is hard to explain, it’s a bad idea.
   如果一个实现很难解释清楚，说明实现的idea有问题。
1. If the implementation is easy to explain, it may be a good idea.
   如果一个实现很容易解释清楚，那可能是个好的实现idea。
1. NameSpaces are one honking great idea – let’s do more of those!
   Namespace真真儿是个好想法 — 放手多多使用吧！

### 译注
- 【1】【2】 单词complex的意思是 复杂，而complicated 是 结构复杂。
- 在计算机中，单个模块复杂理解为complex，而多个模块互相关联的复杂理解为complicated。用计算机的术语，complicated是模块之间“耦合”很多，说明理解不深，设计不好。
- 软件的核心复杂度不可避免，但要这些集中一起，给使用一个干净高级的接口，也就是说：如果complex（核心复杂度）不可避免可以接受，但complicated一定要想办法去除，随着系统深入理解，模块职责的划分会更简明干净。 PS： 核心复杂度的说明讨论可以参见《代码大全》一书。
- 翻译上，complex翻成 复杂，complicated翻成 纠结。
- 【3】 稀疏、稠密指的是代码行中操作的疏密。C的Geek，喜欢写稠密的代码，比如使用++，–运算符来压缩代码行。在Python看来，这个做法不可取，即会让代码更可能出错（如自增操作的负作用），也降低了代码的可读性。
- 【4】 这里的荷兰人指Python 之父Guido，参见说明：http://qianjigui.javaeye.com/blog/266365

参考/阅读资料
Python Philosophy原文 http://www.c2.com/cgi/wiki?PythonPhilosophy
No programming language offers what Python does philosophically. PS：没有一门编程语言做到了Python在编程哲学上所做的。
Python(programming language) - Wikipedia
武汉大学开源技术俱乐部 技术交流 第1期 http://qianjigui.javaeye.com/blog/266365。(这里还有其它有关Python有意思的东西)
核心复杂度的说明参见《代码大全》一书。
