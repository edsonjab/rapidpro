FROM mvilchis/rapidpro-base:v1.0
MAINTAINER Miguel Vilchis "mvilchis@ciencias.unam.mx"


#################  Enviroment variables  #################
ENV C_FORCE_ROOT True
ENV UWSGI_WSGI_FILE=temba/wsgi.py
ENV UWSGI_HTTP=:8000
ENV UWSGI_MASTER=1
ENV UWSGI_WORKERS=8
ENV UWSGI_HARAKIRI=20
ENV LANG C.UTF-8
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone



#################     Install packages    #################
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  bash \
  patch \
  git \
  gcc \
  g++ \
  make \
  libc-dev \
  musl-dev \
  libpng-dev \
  libxslt-dev \
  libxml2-dev \
  libffi-dev \
  ncurses-dev \
  nodejs \
  npm \
  nodejs-legacy \
  python \
  python-setuptools \
  python-pip \
  python-dev \
  build-essential \
  vim \
  wget \
  libpq-dev \
  file \
  lib32ncurses5-dev \
  libgeos-dev && \
  rm -rf /var/lib/apt/lists/* && \
  npm install -g less && \
  npm install -g coffee-script && \
  npm install -g bower

#RUN apt-get install -y --no-install-recommends postgresql-client




#################     Work directory     #################
RUN mkdir rapidpro
WORKDIR /rapidpro
COPY pip-freeze.txt /rapidpro
COPY pip-requires.txt /rapidpro
#################    Old dependencies    #################
# For broken dependency to old Pillow version from django-quickblocks
RUN sed -i '/Pillow/c\Pillow==3.4.2' /rapidpro/pip-freeze.txt
# dj-database-url does not work with sqlite://:memory: url which is needed for build mode.
RUN sed -i '/dj-database-url/c\dj-database-url==0.4.1' /rapidpro/pip-freeze.txt

#################   Install requirements  #################
RUN pip install --upgrade pip==9.0.3 && \
  pip install --upgrade setuptools && \
  pip install -r pip-freeze.txt

ADD . /rapidpro
RUN cp temba/settings.py.dev temba/settings.py
#################    Set configuration    #################

RUN sed -i 's/sitestatic\///' /rapidpro/static/brands/rapidpro/less/style.less
RUN sed -i '/                - for obj in object_list/c\                - for obj in object_list\n \                  - if obj.id >= 0' templates/smartmin/list.haml
EXPOSE 8000
EXPOSE 5555

CMD ["./start.sh"]
