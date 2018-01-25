# fxdayu_dataz

rqalpha工具包，用于抓取tdx等数据并合成K线数据写入MongoDB。

# !!! 尚未开发完毕，以下为参考原项目文档的说明。

## 用pip安装

> pip install git+https://github.com/crystalphi/fxdayu_dataz.git

## 初始化

### 创建配置文件
PATH为要存储文件的目录
> dataz init config PATH
可以通过添加环境变量FXDAYU来指定配置文件的目录
例如添加环境变量FXDAYU=~/fxdayu，配置文件会生成在~/fxdayu/dataz/目录中

### 创建文件索引
可以用参数 -s yyyy-mm-dd, -e yyyy-mm-dd 指定索引长度
> dataz init create

## 下载tick数据

可以用参数 -s yyyy-mm-dd, -e yyyy-mm-dd 指定请求范围
> dataz request tick

下载数据所用时间可能较长，可以先指定一段较短时间的数据测试。

## 根据tick数据文件更新主索引：
> dataz master file

## 将tick数据整理成一分钟数据写入数据库
> dataz write master

## 根据数据库更新主索引
> dataz master db

## 扩展主索引
可用参数 -s yyyy-mm-dd, -e yyyy-mm-dd 指定扩展范围
> dataz master update


