FROM ubuntu:20.04

# backend and models
WORKDIR /opt/backend
COPY . .

# package
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends\
    python3.9 \
    python3-pip \
    python3-setuptools\
    sqlite3

# バックエンド向けの記述（pipenv install するためにあれこれ）
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN /usr/bin/python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

# バックエンドサーバ実行 (実行場所をdjangoのmanage.pyがある階層にする)
WORKDIR /opt/backend/janten_master/
CMD ["/usr/bin/python", "/opt/backend/janten_master/manage.py", "runserver", "0:8000"]