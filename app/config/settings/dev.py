# 1. dev.json
# 2. settings.dev
#   set_config() <- 이거 쓰세요
# 3. wsgi.dev
# 4. .config/dev/ 파일들
#   4.1. nginx-app.conf
#   4.2. uwsgi.ini
#   4.3. supervisord.conf
# 5. Dockerfile.dev
#   5.1. ENV를 사용해 환경변수 설정
#   5.2. docker build에서 migrate 및 createsu제외
# 6. docker build eb-docker:dev
from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'
INSTALLED_APPS += [
    'django_extensions',
]

set_config(secrets, module_name=__name__, start=True)
print(getattr(sys.modules[__name__], 'DATABASES'))
