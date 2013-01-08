# Local settings for {{ project_name }} project.
LOCAL_SETTINGS = True
from settings import *
DEBUG = True
TEMPLATE_DEBUG = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # We use the debug toolbar only if DEBUG is True
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

    DEBUG_SCSS_LIST = [
        'main/scss/_*.scss',
        'main/scss/**/_*.scss',
    ]

    PIPELINE_CSS['style']['source_filenames'].extend(DEBUG_SCSS_LIST)

    MIDDLEWARE_CLASSES.remove('pipeline.middleware.MinifyHTMLMiddleware')
