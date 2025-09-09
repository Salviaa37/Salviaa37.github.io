AUTHOR = 'salviaa37'
SITENAME = 'Salviaa37`s Home'
SITEURL = "https://salviaa37.github.io/"

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'

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

# 主题设置
THEME = "./pelican-themes/pelican-alchemy/alchemy"

# 代码高亮
PYGMENTS_STYLE = 'default'

# 网站描述
DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
              'inspired by crowsfoot and clean-blog, powered by Bootstrap.'
              
# 使用文件夹分类
USE_FOLDER_AS_CATEGORY = True

# 插件
PLUGIN_PATHS = ["./plugins"]
PLUGINS = ['pelican-page-hierarchy']

# 页面分级
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

# sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
