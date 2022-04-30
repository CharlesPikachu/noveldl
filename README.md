<div align="center">
  <img src="./docs/logo.png" width="600"/>
</div>
<br />

[![docs](https://img.shields.io/badge/docs-latest-blue)](https://noveldl.readthedocs.io/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/noveldl)](https://pypi.org/project/noveldl/)
[![PyPI](https://img.shields.io/pypi/v/noveldl)](https://pypi.org/project/noveldl)
[![license](https://img.shields.io/github/license/CharlesPikachu/noveldl.svg)](https://github.com/CharlesPikachu/noveldl/blob/master/LICENSE)
[![PyPI - Downloads](https://pepy.tech/badge/noveldl)](https://pypi.org/project/noveldl/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/noveldl?style=flat-square)](https://pypi.org/project/noveldl/)
[![issue resolution](https://isitmaintained.com/badge/resolution/CharlesPikachu/noveldl.svg)](https://github.com/CharlesPikachu/noveldl/issues)
[![open issues](https://isitmaintained.com/badge/open/CharlesPikachu/noveldl.svg)](https://github.com/CharlesPikachu/noveldl/issues)

Documents: https://noveldl.readthedocs.io/


# NovelDL

```
Search and download novels from some specific websites.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```


# Support List

|  Source_EN                          |  Source_CN       |   Support Search?  |  Support Download?   |
|  :----:                             |  :----:          |   :----:           |  :----:              |
|  [zw81](https://www.81zw.com/)      |  八一中文网      |   ✓                |  ✓                   |
|  [gebiqu](https://www.gebiqu.com/)  |  阁笔趣          |   ✓                |  ✓                   |


# Install

#### Pip install

```
run "pip install noveldl"
```

#### Source code install

```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/noveldl.git
Step2: cd noveldl -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/noveldl.git@master"
```


# Quick Start

#### Run by leveraging the API

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

#### Run by leveraging compiled file

```

```


# Screenshot

![img](./docs/screenshot.gif)


# Projects in Charles_pikachu

- [Games](https://github.com/CharlesPikachu/Games): Create interesting games by pure python.
- [DecryptLogin](https://github.com/CharlesPikachu/DecryptLogin): APIs for loginning some websites by using requests.
- [Musicdl](https://github.com/CharlesPikachu/musicdl): A lightweight music downloader written by pure python.
- [Videodl](https://github.com/CharlesPikachu/videodl): A lightweight video downloader written by pure python.
- [Pytools](https://github.com/CharlesPikachu/pytools): Some useful tools written by pure python.
- [PikachuWeChat](https://github.com/CharlesPikachu/pikachuwechat): Play WeChat with itchat-uos.
- [Pydrawing](https://github.com/CharlesPikachu/pydrawing): Beautify your image or video.
- [ImageCompressor](https://github.com/CharlesPikachu/imagecompressor): Image compressors written by pure python.
- [FreeProxy](https://github.com/CharlesPikachu/freeproxy): Collecting free proxies from internet.
- [Paperdl](https://github.com/CharlesPikachu/paperdl): Search and download paper from specific websites.
- [Sciogovterminal](https://github.com/CharlesPikachu/sciogovterminal): Browse "The State Council Information Office of the People's Republic of China" in the terminal.
- [CodeFree](https://github.com/CharlesPikachu/codefree): Make no code a reality.
- [DeepLearningToys](https://github.com/CharlesPikachu/deeplearningtoys): Some deep learning toys implemented in pytorch.
- [DataAnalysis](https://github.com/CharlesPikachu/dataanalysis): Some data analysis projects in charles_pikachu.
- [Imagedl](https://github.com/CharlesPikachu/imagedl): Search and download images from specific websites.
- [Pytoydl](https://github.com/CharlesPikachu/pytoydl): A toy deep learning framework built upon numpy.
- [NovelDL](https://github.com/CharlesPikachu/noveldl): Search and download novels from some specific websites.


# More

#### WeChat Official Accounts

*Charles_pikachu*  
![img](./docs/pikachu.jpg)