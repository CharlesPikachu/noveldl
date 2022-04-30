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