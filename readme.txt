本文档是本项目的备注说明
声明:本代码只用于技术交流之用
请勿恶意爬取网站致使损害公共利益行为的发生.
未经允许,不得传播和将代码用于商业途径

语言:Python
涉及的库:
request
csv
re
os
beautifulsoup

注意
这是一个利用某家日报的URL命名规则对某家日报的网站进行纯文字内容爬取的小爬虫
只有源代码,不提供接口.
这是笔者半年前完成的项目,考虑到编写代码的难度,笔者当时的水平等诸多因素,代码中缺少异常和对异常的捕获,没有经过优良的设计,命名规则一塌糊涂,也夹杂着相对地址和绝对地址的混用.虽然如此,笔者还是批处理完成了相当大量的文件,是笔者个人的一个里程碑.
这份代码没有随着目标网站的编码方式的改变而改变,因此可能不太好用.
请小心使用,避免翻车.

Date.py
无输入
在相同目录下生成Date.txt文件以"MMDD"格式生成日期,一个日期一行.

Paurl.py
打开相同目录下的Date.txt文件.
批处理每行的以"MMDD"格式以获得2019年该日某日报的文章标题和对应的URL的一部分
生成rbMMDD.csv和rbMMDD.txt两个文件

newfilecopy.py
打开相同路径下的Date.txt文件,对于"MMDD"格式的日期进行批处理
对于这样的日期打开相关的rb文件,批处理其每一篇文章.
对于每一篇文章,寻找有汉字的标签
保存在./Article/MMDD/MMDD_index下,index为当日的第index篇文章并且count from zero
将每一天的文章数量以MMDD_index形式放在同一路径下number.txt文件中.

Arti.py
打开相同路径下的Date.txt文件,对于"MMDD"格式的日期进行批处理
对于这样的日期打开相关的rb文件,批处理其每一篇文章.
对于每一篇文章,寻找有汉字的标签
保存在./Article/MMDD/MMDD_index下,index为当日的第index篇文章并且count from zero

GilbertTrumpTrunks
于2020.6.20
