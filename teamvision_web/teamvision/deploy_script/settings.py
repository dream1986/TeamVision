# coding=utf-8
"""
Django settings for teamvision project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + r"/teamvision"
ROOT_DIR = "/web/www/teamvision/teamvision"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3m4+k9yf02#+2g1$z!3_fly@x*27daj#9+0zpb)ad$thb)_kon'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['teamvision.qyvideo.net', '10.69.58.195']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #     'teamvision.testcase',
    #     'teamvision.automationtesting',
    #     'teamvision.testjob',
    #     'teamvision.userauthority',
    'teamvision.ci',
    'teamvision.api',
    'teamvision.home',
    'teamvision.project',
    'teamvision.auth_extend.user',
    'teamvision.user_center',
    'teamvision.administrate',
    'teamvision.device',
    'teamvision.logcat',
    'ws4redis',
    'rest_framework',
    'rest_framework_mongoengine',
    'rest_framework_docs',
    'rest_framework.authtoken',
    'crispy_forms',
    'django_filters',
    'oauth2_provider',
    'corsheaders',
)

MIDDLEWARE = (
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
)

ROOT_URLCONF = 'teamvision.urls'

WSGI_APPLICATION = 'teamvision.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'teamvision_nirvana',
        'USER': 'teamvision',
        'PASSWORD': 'Nopass.2',
        'HOST': '127.0.0.1',
        'PORT': '8001',
    },
}

MONGODB = {
    'default': {
        'HOST': "10.69.59.119",
        'PORT': 8807,
        'DB': 'teamvision',
        'ALIAS': 'teamvision'
    },
    'log': {
        'HOST': "10.69.59.119",
        'PORT': 8807,
        'DB': 'teamvision_log',
        'ALIAS': 'teamvision_log'
    },
    'archive': {
        'HOST': "10.69.59.119",
        'PORT': 8807,
        'DB': 'teamvision_archive',
        'ALIAS': 'teamvision_archive'
    },
    'release_archive': {
        'HOST': "10.69.59.119",
        'PORT': 8807,
        'DB': 'teamvision_release_resp',
        'ALIAS': 'release_resp'
    },
    'project_documents': {
        'HOST': "10.69.59.119",
        'PORT': 8807,
        'DB': 'teamvision_project_doc',
        'ALIAS': 'project_documents'
    },
    'project_issue': {
        'HOST': "10.69.59.119",
        'PORT': 8807,
        'DB': 'teamvision_project_issue',
        'ALIAS': 'project_issue'
    },
    'env_mock': {
        'HOST': "10.69.59.119",
        'PORT': 8807,
        'DB': 'teamvision_env_mock',
        'ALIAS': 'env_mock'
    }
}

REDIS = {
    'default': {
        "HOST": "127.0.0.1",
        "PORT": 8803,
        "DB": 0,
        "EXPIRE": 7200
    },
    'build_log': {
        "HOST": "127.0.0.1",
        "PORT": 8803,
        "DB": 0,
        "EXPIRE": 7200
    },
    'file_cache': {
        "HOST": "127.0.0.1",
        "PORT": 8803,
        "DB": 1,
        "EXPIRE": 7200
    }
}

REDIS_HOST = "127.0.0.1"
REDIS_HOST_PORT = 8803

EMAILCONFIG = {
    'HOST': 'smtp.kingsoft.com',
    'PORT': 25,
    'USER': 'gedqa',
    'PASSWORD': '',
    'ISAUTH': False,
    'STARTSSL': False,
    'POSTFIX': 'kingsoft.com'
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# MEDIA_ROOT = ''
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/').replace('\\', '/')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA_URL = ''
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/collect_files').replace('\\', '/')
STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
# add property : ADMIN_MEDIA_ROOT BY slider
# ADMIN_MEDIA_ROOT = '/static/admin/' 
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)

AUTHENTICATION_BACKENDS = (

    'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static\\global\\templates').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ws4redis.context_processors.default',
            ],
            'builtins': ['teamvision.auth_extend.user.templatetags.auth_required',
                         'teamvision.auth_extend.user.templatetags.project_role_required'
                         ],
        },
    },
]

# This setting is required to override the Django's main loop, when running in
# development mode, such as ./manage runserver
WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# URL that distinguishes websocket connections from normal requests
WEBSOCKET_URL = '/ws/'

# Set the number of seconds each message shall persited
WS4REDIS_EXPIRE = 3600

WS4REDIS_HEARTBEAT = '--heartbeat--'

WS4REDIS_PREFIX = 'ci-log'

WS4REDIS_CONNECTION = {
    'host': '127.0.0.1',
    'port': 8803
}

BASE_DIR_TEST = "/web/www/teamvision/teamvision"
EMAIL_TEMPLATES = {
    "ForTesting": BASE_DIR_TEST + '/static/project/contents/commit_testing_emailtemplate.html'.replace('\\', '/'),
    "BuildPackage": os.path.join(BASE_DIR_TEST, '/static/project/contents/build_package_emailtemplate.html').replace(
        '\\', '/'),
    "ParameterGroupChangedPage": BASE_DIR_TEST + '/static/ci/contents/task_parameter_group_notification.html'.replace(
        '\\', '/'),
    "ParameterGroupChangedDetail": BASE_DIR_TEST + '/static/ci/contents/task_parameter_group_change_detail.html'.replace(
        '\\', '/'),
    "TestingFinished": BASE_DIR_TEST + '/static/project/contents/testing_finished_emailtemplate.html'.replace('\\',
                                                                                                              '/'),
    "InTesting": BASE_DIR_TEST + '/static/project/contents/in_testing_emailtemplate.html'.replace('\\', '/'),

    "Issue":BASE_DIR_TEST+'/static/project/contents/issue_status_changed_emailtemplate.html'.replace('\\','/'),
}

DATABASE_ROUTERS = ['teamvision.automationtesting.datamodels.automationtaskdbrouter.AutomationTaskDBRouter',
                    'teamvision.productquality.datamodels.productqualitydbrouter.ProductQualityDBRouter']

LOGIN_URL = "/user/login"
LOG_CONFIG = ('/web/www/teamvision/teamvision/logconfig.conf').replace('\\', '/')
WEB_HOST = "http://teamvision.qyvideo.net"
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        #         'rest_framework.permissions.IsAuthenticated',
    ],
    #     'PAGE_SIZE': 5,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #         'rest_framework.authentication.TokenAuthentication',
        #         'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ],
    #     'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_RENDERER_CLASSES': (
        #         'rest_framework.renderers.JSONRenderer',
        'teamvision.api.api_render.TeamvisionJSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'url_filter.integrations.drf.DjangoFilterBackend',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    #     'DEFAULT_VERSION':'fdsfds.0'
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
