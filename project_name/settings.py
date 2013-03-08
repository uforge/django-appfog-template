# Global settings for {{ project_name }} project.
import os

PROJECT_DIR = os.path.dirname(__file__)
PUBLIC_DIR = os.path.join(PROJECT_DIR, 'public')

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Maksim Sinik', 'max@droidware.it'),
    ('Luca Del Bianco', 'luca@droidware.it')
)

MANAGERS = ADMINS

## Pull in CloudFoundry's production settings
if 'VCAP_SERVICES' in os.environ:
    import json
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    # XXX: avoid hardcoding here
    mysql_srv = vcap_services['mysql-5.1'][0]
    cred = mysql_srv['credentials']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': cred['name'],
            'USER': cred['user'],
            'PASSWORD': cred['password'],
            'HOST': cred['hostname'],
            'PORT': cred['port'],
            }
        }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(PROJECT_DIR, "{{ project_name }}.db"),
            "USER": "",
            "PASSWORD": "",
            "HOST": "",
            "PORT": "",
            }
        }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Secret key needed by django >= 1.4
SECRET_KEY = '{{ secret_key }}'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#   Uncomment this to minify the HTML
    'pipeline.middleware.MinifyHTMLMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, 'fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Used to maintain the database and do migrations
    'south',
    # Used to autocompile scss/eco/coffee files
    'pipeline',
    # Our main application
    'apps.main',
    'droid.commonjs',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_CSS = {
    'style': {
        'source_filenames': [
          'main/scss/style.scss',
        ],
        'output_filename': 'main/css/style.css',
    },
    'screen': {
        'source_filenames': [
          'main/scss/screen.scss',
        ],
        'output_filename': 'main/css/screen.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'print': {
        'source_filenames': [
          'main/scss/print.scss',
        ],
        'output_filename': 'main/css/print.css',
        'extra_context': {
            'media': 'print',
        },
    },
    'ie': {
        'source_filenames': [
          'main/scss/ie.scss',
        ],
        'output_filename': 'main/css/ie.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

# We first include the assets in a single file called assets.js and then we add our 
# sources to a file called application.js
PIPELINE_JS = {
    'assets': {
        'source_filenames': [
            'main/js/assets/libs/*.coffee',
            'main/js/assets/libs/jquery.js',
            'main/js/assets/libs/underscore.js',
            'main/js/assets/libs/backbone.js',
            'main/js/assets/libs/*.js',
            'main/js/assets/plugins/*.coffee',
            'main/js/assets/plugins/*.js',

            'main/bootstrap/js/*.min.js',
        ],
        'output_filename': 'main/js/assets.js'
    },
# This is the real application, uncomment this lines if you use the default structure
    'application': {
        'source_filenames': [
#            'main/js/app/namespace.coffee',
#            'main/js/app/modules/*.coffee',
#            'main/js/app/templates/*.eco',
#            'main/js/app/index.coffee',
        ],
        'output_filename': 'main/js/application.js'
    },
}

PIPELINE_COMPILERS = (
    'pipeline_compass.compiler.CompassCompiler',
    'pipeline_eco.compiler.EcoCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

PIPELINE_AUTO = False
PIPELINE_VERSION = True
PIPELINE_VERSION_PLACEHOLDER = 'VERSION'
PIPELINE_VERSIONING = 'pipeline.versioning.hash.SHA1Versioning'

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        pass
