# markdown图床外链图片下载到本地代码

## 前言

> 因为文章发到先知或者攻防社区需要本地图片，而我的图片从来都是上传到图床，所以编写了一个脚本实现了把markdown文章中所有含有外链图床的图片转储到本地的文件夹。
> 然后发布文章时再手动一个个上传图片(关于这个问题有看到本篇文章的大哥有什么好办法也可以教教弟弟)。

## 代码

`download_images_from_markdown.py`

```python
import re
import requests
import os

# 定义要匹配的 Markdown 文件路径
markdown_file = 'F:\Desktop\恶意程序快速分析—脚本类和文档类.md'

# 定义保存图片的本地文件夹
local_folder = 'F:\Desktop\markdown外链转存图片\恶意程序 脚本和文档类'

# 创建本地文件夹
if not os.path.exists(local_folder):
    os.makedirs(local_folder)

# 读取 Markdown 文件内容
with open(markdown_file, 'r', encoding="utf-8") as file:
    content = file.read()

# 使用正则表达式匹配图片链接
image_urls = re.findall(r'!\[.*?\]\((.*?)\)', content)

# 下载图片
for url in image_urls:
    response = requests.get(url)
    if response.status_code == 200:
        image_name = url.split('/')[-1]
        image_path = os.path.join(local_folder, image_name)
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded: {image_name}')
    else:
        print(f'Failed to download: {url}')

```

## 运行

直接在pycharm中运行或者命令

或者在控制台中

```
python download_images_from_markdown.py
```

## 示例

![58a44d3b6d870f6347b5d0407703dd2](https://cdn.jsdelivr.net/gh/SlientRainyDay/image@main/image/202403271648603.png)

## 注意

可能是笔者使用的是github作为图床的原因，转储时要关闭梯子(因为这个出现的其他问题还不少)，不然会报错。
