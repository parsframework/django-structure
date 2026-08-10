from pathlib import Path





BASE_DIR=Path(__file__).resolve().parent.parent


SECRET_KEY='MY_SECRET_KEY'


DEBUG=True
ALLOWED_HOSTS=[]


INSTALLED_APPS=[
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'django.contrib.sites',
'django.contrib.sitemaps',
'db',
#'api',
'account',
'dashboard',
'main',
]
SITE_ID=1


MIDDLEWARE=[
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.locale.LocaleMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF='setting.urls'


TEMPLATES=[
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
]


WSGI_APPLICATION='setting.wsgi.application'


DATABASES={
'default':{
'ENGINE':'django.db.backends.sqlite3',
'NAME':BASE_DIR/'db.sqlite3',
}
}


AUTH_PASSWORD_VALIDATORS=[
{
'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
},
]


USE_I18N=True
LANGUAGE_CODE='en-US'
LANGUAGES=[
('en-US','English'),
]
LOCALE_PATHS=[
BASE_DIR/'Languages/',
]


TIME_ZONE='UTC'
USE_TZ=True
#USE_L10N=False
#USE_THOUSAND_SEPARATOR=False


STATIC_URL='static/'
STATICFILES_DIRS=[BASE_DIR/'assets',]
STATIC_ROOT=BASE_DIR/'staticfiles'
STATICFILES_FINDERS=['django.contrib.staticfiles.finders.AppDirectoriesFinder','django.contrib.staticfiles.finders.FileSystemFinder',]
MEDIA_ROOT=BASE_DIR/'assets/uploads/'
MEDIA_URL='/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL='db.User'


LOGIN_URL='auth/login/'
LOGIN_REDIRECT_URL='/dashboard/'
LOGOUT_URL='/auth/logout'
LOGOUT_REDIRECT_URL=LOGIN_URL


EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.MY_MAIL.com'
EMAIL_PORT='MY_PORT'
EMAIL_USE_TLS=True
EMAIL_HOST_USER='MY_NAME@MY_MAIL.com'
EMAIL_HOST_PASSWORD='MY_PASSWORD'
