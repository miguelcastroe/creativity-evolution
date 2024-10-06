# pelicanconf.py

AUTHOR = 'Miguel Castro'
SITENAME = 'Creativity Evolution'
SITEURL = ''

# Path to content
PATH = 'content'

# Timezone and language settings
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

# Feed generation (disable during development)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll (Links section)
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

# Social widget (Add your social media links here)
SOCIAL = (
    ('GitHub', 'https://github.com/miguelcastroe'),
    # Add more social links here
)

# Default settings
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Output path for generated site
OUTPUT_PATH = 'output/'
