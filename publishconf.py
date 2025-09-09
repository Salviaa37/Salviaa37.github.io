# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# 生产环境站点根（GitHub Pages 用户名仓库）
SITEURL = "https://salviaa37.github.io"
# 生产环境不要使用相对 URL
RELATIVE_URLS = False

# 开启 Feed 输出（可按需关闭）
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# 推荐：避免把不必要文件放进输出
OUTPUT_RETENTION = ['.git']

# 如果需要 Google Analytics / 评论，可在这里配置
# GOOGLE_ANALYTICS = "G-XXXXXXXXXX"
# DISQUS_SITENAME = "your-disqus-shortname"


# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
