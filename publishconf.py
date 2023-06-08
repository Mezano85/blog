from datetime import date

AUTHOR = 'Francisco G. Mezano'
SITENAME = 'Blog DataOps!!'
SITEPATH = 'blog'
SITEURL = f'https://mezano85.github.io/{SITEPATH}'


PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_SAVE_AS = 'archives.html'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/blue_one'


# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2022
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Hello world! I’m John Doe.'
AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
AUTHOR_AVATAR = 'https://media.licdn.com/dms/image/C4E03AQGCo0TsMjrGKw/profile-displayphoto-shrink_200_200/0/1599577226305?e=1691625600&v=beta&t=6B2UXhqNmuizRMSaDDWxMqRXmQVeDIJZ2fEg9AkVTRE'
AUTHOR_WEB = 'http://mypersonalsite.com'

# Services
GOOGLE_ANALYTICS = 'UA-12345678-9'
#DISQUS_SITENAME = 'johndoe'

# Social
SOCIAL = (
    ('facebook', 'http://www.facebook.com/johndoe'),
    ('twitter', 'http://twitter.com/johndoe'),
    ('github', 'https://github.com/johndoe'),
    ('linkedin', 'http://www.linkedin.com/in/mezano'),
)

DISPLAY_CATEGORIES_ON_MENU = False

# Menu
MENUITEMS = (
    ('Categories', f'{SITEPATH}/{CATEGORIES_SAVE_AS}'),
    ('Archive', f'{SITEPATH}/{CATEGORIES_SAVE_AS}'),
)
