# 命令行获取磁力工具

*作为一个理工宅男,找磁链是非常经常的事情,比如找新出的电影这些对吧<- <-,为了方便,就自己写了一个简单的查询工具*

## 兼容环境
`Windows/Linux/MacOs`

## 安装
### 源码安装

```
 $ git clone https://github.com/cexll/cilimao-cli.git
 $ cd cilimao-cli
 $ pip install -r requirements.txt
 $ python setup.py install
```

## 如何使用
```
$ cilimao-cli -h
命令行磁力猫查询
默认选择按视频排序,按下载热度排序

Usage:
    cilimao [-p] <KEYWORD>
    cilimao [-h,--help]   显示帮助菜单

Options:
    -h,--help       显示帮助菜单
    -p              页数(默认为0)

Example:
    cilimao 复仇者联盟
    cilimao -p 1 复仇者联盟
```

## 示例
### 根据关键词搜索
```
$ cilimao-cli 战狼2
Crawling data for you.....
磁链标题:  战狼2
磁链地址: magnet:?xt=urn:btih:63116E5EF0D8A811521AEE5CCBE68F8BF9372051
文件数目:  1
文件大小:  1.085152080282569GB
创建时间:  2017-08-16 02:57:12

磁链标题:  战狼2
磁链地址: magnet:?xt=urn:btih:638B206F3FB1BDAAF7C3A2DEB876D7D173BE1F5F
文件数目:  2
文件大小:  2.75575786922127GB
创建时间:  2017-10-26 13:29:03

磁链标题:  战狼2
磁链地址: magnet:?xt=urn:btih:902C4B0D02BECA80C7CB7210A18769A7B6B26678
文件数目:  2
文件大小:  1.139014646410942GB
创建时间:  2017-09-17 05:39:05

磁链标题:  战狼2
磁链地址: magnet:?xt=urn:btih:4C9B11CA3A380CC49A7D54FFF0CD664A1207D861
文件数目:  2
文件大小:  1.9200079273432493GB
创建时间:  2017-10-13 21:00:44

磁链标题:  战狼2
磁链地址: magnet:?xt=urn:btih:163AEA5F60E81665C159CB2882867D2491A0D845
文件数目:  2
文件大小:  1.139014646410942GB
创建时间:  2017-08-17 23:25:03

磁链标题:  战狼2
磁链地址: magnet:?xt=urn:btih:773684B47D4EA898675B1B91FAECD656CA4709A9
文件数目:  2
文件大小:  1.9201079765334725GB
创建时间:  2017-08-28 07:35:34
......
```

## License
MIT [©cexll](https://github.com/cexll)
