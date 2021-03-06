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

# Bucket생성
# storage.py에 적절히 스토리지 생성
# 사용설정
# collectstatic
# 완-성
from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
set_config(secrets, module_name=__name__, start=True)

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
]
WSGI_APPLICATION = 'config.wsgi.dev.application'
INSTALLED_APPS += [
    'django_extensions',
    'storages',
]
# S3대신 EC2에서 정적파일을 제공 (프리티어의 Put사용량 절감)
# STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
