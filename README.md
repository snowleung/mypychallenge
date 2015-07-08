# mypychallenge
let's rock!!!!


###L0
* just 2**38

###L1
* +2 know in pic
* y->a, z->b know in tips
* use trans table is better.

###L2
* http://www.pythonchallenge.com/pc/def/ocr.html
* use find characters parttern => '[a-zA-Z]'
* （答案由）找到的字母组成

###L3
* http://www.pythonchallenge.com/pc/def/equality.html
* （答案由）一个由三个大写字母围绕着一个小写组合而成(即SSSaSSS，匹配其中的a)

###L4
* 循环nothing，直到出错，不停的利用提示的next进行请求

###L5
* peak hell sounds familiar ?  pickle.........(看答案才知道的)
* req -> http://www.pythonchallenge.com/pc/def/banner.p （在源码中）
* pickle.load(req)
* 发现是一个二维数组, 内容是(待打印的字符, 打印次数)，然后print它出来得出答案。（这里有个巧妙就是str*int ）

###L6
* channel.html -> channel.zip得到源文件（看了答案才知道）
* 使用的是zipfile模块

###7
* oxygen.png 找到中间灰色的
* 从l7联想到间隔是7（看答案的）
* 用getpixel找x间隔是7的值得出数字，转为asc2得出结果
* 再将结果中的数字转为asc2的字符得出最终结果

###8
* bee? busy? ------------> bz2 （果断看答案）
* un, pw用bz2解即可知道用户名密码，然后点图片的链接去登陆


###9
* first+second? 其实first和second都分别隐含了(x, y), start=0, setp=2是x, start=1, step=2是y然后得出两条线，将这两条线画出来就看到一只公牛(bull)（看答案才知道的）
* 所以first+second代表线条first+线条second得出一幅画
