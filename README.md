# fxdayu_dataz

rqalpha工具包，用于抓取tdx等数据并合成K线数据写入MongoDB。


## 用pip安装

> rm -rf `python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`/fxdayu_dataz*
> pip install git+https://github.com/crystalphi/fxdayu_dataz.git


## 初始化

### 创建配置文件
> dataz init config PATH
PATH为要存储文件的目录，如：~/.fxdayu/dataz_bundle
可以通过添加环境变量FXDAYU来指定配置文件的目录
例如添加环境变量FXDAYU=~/.fxdayu，配置文件会生成在~/.fxdayu/dataz/目录中

### 创建文件索引
可以用参数 -s yyyy-mm-dd, -e yyyy-mm-dd 指定索引长度
> rm -rf  ~/.fxdayu/dataz_bundle/* （可选）
> dataz init create -s 2018-01-01 -e 2018-01-05


## 从新浪下载tick数据（更新不及时，下载不稳定，数据质量不如 tdx）

TODO 需要改为从 tdx 获取!!

可以用参数 -s yyyy-mm-dd, -e yyyy-mm-dd 指定请求范围
注：如果前面的文建索引范围较大，在这里缩小范围则无效
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


