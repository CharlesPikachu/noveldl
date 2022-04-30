# 快速开始

#### API调用

示例代码如下:

```python
from noveldl import noveldl

config = {
    'savedir': 'outputs',
    'search_size_per_source': 5,
    'proxies': {},
}
client = noveldl.noveldl(config=config)
client.run()
```

config中的参数解释如下:

- savedir: 小说保存的文件夹;
- search_size_per_source: 在每个小说网站源上最多搜索的小说数量;
- proxies: 设置代理, 支持的代理格式参见[Requests](https://requests.readthedocs.io/en/master/user/advanced/#proxies)。

run函数支持的参数如下:

- target_src: 使用的小说网站源, 目前支持"zw81"和"gebiqu"。

#### 编译调用

pip安装之后, 环境变量中会自动生成noveldl.exe文件, 只需要在终端直接输入noveldl即可调用, 使用方式如下:

```sh
Usage: noveldl [OPTIONS]

Options:
  --version           Show the version and exit.
  -k, --keyword TEXT  想要搜索下载的小说关键字, 若不指定, 则进入noveldl终端版
  -p, --proxies TEXT  设置的代理
  -s, --savedir TEXT  下载的小说的保存路径
  -c, --count TEXT    在各个平台搜索时的小说搜索数量
  -t, --targets TEXT  指定小说搜索下载的平台, 例如"zw81,gebiqu"
  --help              Show this message and exit.
```

例如:

```sh
noveldl -k 焦裕禄
```

效果如下:

<div align="center">
  <img src="https://github.com/CharlesPikachu/noveldl/raw/main/docs/screenshot.gif" width="600"/>
</div>
<br />