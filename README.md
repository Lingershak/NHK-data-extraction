# NHK-data-extraction
This is mainly used to extract audio data from NHK

最終の目的はNHKのニュース自分のパソコンにドンウォンします。


### 阶段一：

实现从页面上下载一个mp3文件，路径是跟随默认，命名是固定写死。

### 问题：

+ 1.没有预防机制，路径错误，服务器未响应等情况出现后，没有报错机制；

+ 2.文件路径不够智能，路径应该要能改成随便设置；

+ 3.文件名称机制不够完善；

+ 4.程序移植性能差，模块化程度不够高；

+ 5.网页请求逻辑限制，智能获取一个；

6. 模拟浏览器发送请求的方式来进行src获取，效率很低

~~~delete~~~

markdown

+ https://www.cnblogs.com/JosephAndGrace/p/6445866.html
