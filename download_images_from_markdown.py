import re
import requests
import os

# 定义要匹配的 Markdown 文件路径
markdown_file = 'F:\Desktop\恶意程序快速分析—脚本类和文档类.md'

# 定义保存图片的本地文件夹
local_folder = 'F:\Desktop\markdown外链转存图片'

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
