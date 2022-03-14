FROM ubuntu:20.04

WORKDIR /app/frontend

COPY . .
#COPY frontend/janten-master/package*.json frontend/janten-master/

# package
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get -y upgrade &&\
    apt-get install -y npm curl &&\
    cd janten-master/ && npm install && npm install -g @vue/cli

# フロントエンド向けの記述
ARG node_ver=16.10.0
ARG node_path=/usr/local/lib/nodejs
ARG node_file_name=node-v${node_ver}-linux-x64
ENV PATH ${node_path}/${node_file_name}/bin:$PATH
## Node.js をダウンロード
RUN curl https://nodejs.org/dist/v${node_ver}/${node_file_name}.tar.xz > ${node_file_name}.tar.xz
## Node.js の各ファイルを /usr/local/lib/nodejs/node-v14.15.4-linux-x64/ に解凍
RUN mkdir -p $node_path
RUN tar xJvf ${node_file_name}.tar.xz -C $node_path

CMD ["./start.sh"]