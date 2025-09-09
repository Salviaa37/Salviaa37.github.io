AUTHOR = 'salviaa37'
SITENAME = 'Salviaa37`s Home'
# 开发环境建议留空，发布时在 publishconf.py 中覆盖
SITEURL = ""
SITEIMAGE = 'images/68362plsdl.jpg'

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

# 使用符合 Pelican 预期的语言代码（GitHub Pages/Feed 更兼容）
DEFAULT_LANG = 'zh'
# 可选：用于日期/本地化格式
LOCALE = ('zh_CN.UTF-8', 'zh_CN', 'zh')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	("Home", "https://salviaa37.github.io/"),
    ("Github", "https://github.com/Salviaa37"),
    ("Tips", "https://salviaa37.github.io/category/tips.html"),
    ("Resume","https://salviaa37.github.io/category/misc.html"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# 主题设置（开发/生产都用同一主题）
THEME = "./pelican-themes/pelican-alchemy/alchemy"

# 追加自定义样式覆盖（不要直接改主题原始 theme.css，方便以后升级主题）
THEME_CSS_OVERRIDES = [
    'theme/css/custom.css',  # 我们将在主题 static/css 下新建 custom.css
]

# 首页封面背景图（放在 content/images/ 下）
HERO_IMAGE = 'images/cover-wide.jpg'

# 告诉 Pelican 优先使用本项目根下的 templates 目录覆盖主题模板
THEME_TEMPLATES_OVERRIDES = ['templates']

# 代码高亮
PYGMENTS_STYLE = 'default'

# 网站描述
DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
              'inspired by crowsfoot and clean-blog, powered by Bootstrap.'
              
# 使用文件夹分类
USE_FOLDER_AS_CATEGORY = True

# 插件（如需 sitemap，需要安装对应插件后再加入列表）
PLUGIN_PATHS = ["./plugins"]
PLUGINS = [
    'pelican-page-hierarchy',
    # 'sitemap',  # 安装后再取消注释（见发布说明）
]

# 页面分级
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

# 静态资源路径（相对 content/）
STATIC_PATHS = ['images']
# 可选：如果添加 extra 目录存放 CNAME/robots.txt，可如下
# STATIC_PATHS += ['extra']
# EXTRA_PATH_METADATA = {
#     'extra/CNAME': {'path': 'CNAME'},
# }

# sitemap 配置放在这里，确保开发与生产一致（仅在插件可用时生效）
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
}

# 可选 URL 结构（默认即可；如需更短链接可取消注释）
# ARTICLE_URL = '{slug}.html'
# ARTICLE_SAVE_AS = '{slug}.html'

