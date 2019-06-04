# Learning-Python
 Python 学习

 
## 在编程概念种，表达式和语句的区别？ 
- 答: 表达式 (expression) 是被求值的代码，而 语句 (statement) 是一段可执行代码。<br/>
     因为表达式可以被求值，所以它可写再赋值语句等号的右侧。而语句不一定有值，像 import/for/
     break 等语句就不能被用于赋值。<br/>
     表达式本身可以作为表达式语句，也能作为赋值语句的右值或 if 语句的条件等，所以表达式可以作为
     语句的组成部分，但不是必须成分 (e.g.: continue 语句)


- [Google Python 风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/)

### 常用 Linux 命令的基本使用
| 序号 | 命令 | 对应英文 | 作用 |
|:----:|:----:|:----:|:----:|
| 01 | ls | list | 查看当前文件夹下的内容 |
| 02 | pwd | print work directory(打印工作目录) | 查看当前所在文件夹 |
| 03 | cd [目录名] | change directory | 切换文件夹 |
| 04 | touch [文件名] | touch | 如果文件不存在，新建文件 |
| 05 | mkdir [目录名] | make directory | 创面目录 |
| 06 | rm [文件名] | remove | 删除指定的文件名 |
| 07 | clear | clear | 清屏 |


### 在终端中放大/缩小字体:
- 放大: `ctrl + shift + =`
- 缩小: `ctrl + -`

- DSL: Domain Specific Language 的缩写，翻译成中文就是 "特定领域语言"。(例如: html, css, SQL...)
- GPPL: General Purpose Programming Language 即 "通用目标语言"。(例如: C++, Java, Python, JavaScript...)


### Python 安装
- (1) 下载 Python 
- (3) 安装 PyCharm


### Python 注释: 
    + """docstring 文档注释"""
    + ``` # 单行注释 ```

> [一文看懂 Python 面向对象编程 (Python 学习与新手入门必看)](https://mp.weixin.qq
.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483689&idx=1&sn=3c6e345f0dc083450a034a292abcdcba&chksm=a73c6111904be8070fda0c5e64f9263193936aa9e80da13f0f8d77ad6559b431b4d576c0095c&scene=21#wechat_redirect)

### Python 命名规范
 - constant 常量命名      
    ```python
        ACCOUNT = 'qiyue'    
        PASSWORD = '123456'
    ```  
