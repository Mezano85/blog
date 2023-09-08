from datetime import date

AUTHOR = 'Francisco G. Mezano'
SITENAME = 'DataOps Blog'
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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/blue_one'


# Theme customizations
#MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2022
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Hola, soy Francisco García Mezano. DataOps Manager en Nowports.'
AUTHOR_DESCRIPTION = u'Estadístico | Data Scientist | Data Analyst | Data Engineer | Data Team Lead | DataOps Manager'
AUTHOR_AVATAR = 'https://mezano85.github.io/assets/img/profile-img.jpg'
AUTHOR_WEB = 'https://mezano85.github.io/'

# Services
GOOGLE_TAG = 'G-KHB57NQZEG'
#DISQUS_SITENAME = 'johndoe'

# Social
SOCIAL = (
   # ('facebook', 'http://www.facebook.com/johndoe'),
    ('x-twitter', 'https://twitter.com/FranciscoM76995'),
    ('github', 'https://github.com/mezano85'),
    ('linkedin', 'http://www.linkedin.com/in/mezano'),
)

DISPLAY_CATEGORIES_ON_MENU = True

# Menu
#MENUITEMS = (
#    ('Categories', f'{CATEGORIES_SAVE_AS}'),
#    ('Archive', f'{ARCHIVES_SAVE_AS}'),
#)
