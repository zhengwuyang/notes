#Docker 包括三个基本概念
* 镜像（Image）
* 容器（Container）
* 仓库（Repository）
理解了这三个概念，就理解了 Docker 的整个生命周期。

# 镜像
Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。
因为镜像包含操作系统完整的 root 文件系统，其体积往往是庞大的，因此在 Docker 设计时，就充分利用 Union FS 的技术，将其设计为分层存储的架构。
镜像构建时，会一层层构建，前一层是后一层的基础。每一层构建完就不会再发生改变，后一层上的任何改变只发生在自己这一层。比如，删除前一层文件的操作，实际不是真的删除前一层的文件，而是仅在当前层标记为该文件已删除。在最终容器运行的时候，虽然不会看到这个文件，但是实际上该文件会一直跟随镜像。因此，在构建镜像的时候，需要额外小心，每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。

# 安装
用homebrew安装
brew casl install docker
ps:建议去网站下载: 
> https://download.docker.com/mac/stable/Docker.dmg

# 加速器
http://fc3e5ef3.m.daocloud.io

# 获取镜像
docker pull [选项] [Docker Registry地址]<仓库名>:<标签>
* Docker Registry地址：地址的格式一般是 <域名/IP>[:端口号]。默认地址是 Docker Hub。
* 仓库名：如之前所说，这里的仓库名是两段式名称，既 <用户名>/<软件名>。对于 Docker Hub，如果不给出用户名，则默认为 library，也就是官方镜像(Docker Hub)。

`docker pull ubuntu:xenial`
# 启动容器
`docker run -it --rm ubuntu:xenial bash`
docker run 就是运行容器的命令

* -it：这是两个参数，一个是 -i：交互式操作，一个是 -t 终端。我们这里打算进入 bash 执行一些命令并查看返回结果，因此我们需要交互式终端。
* -d 后台运行
* --rm：这个参数是说容器退出后随之将其删除。默认情况下，为了排障需求， 退出的容器并不会立即删除，除非手动 docker             rm。我们这里只是随便执行个命令，看看结果，不需要排障和保留结果，因此使 用 --rm 可以避免浪费空间。
* -p <宿主端口>:<容器端口>，映射宿主端口和容器端口
* ubuntu:xenial：这是指用 ubuntu:xenial镜像为基础来启动容器。
* bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 bash。
进入容器后，我们可以在 Shell下操作，执行任何所需的命令。这里，我们执行了 cat /etc/os-release 查看系统版本

# 进入容器
* docker ps
查看已关闭容器状态: -a
查看ID：-q
* docker stop
* docker start
* docker attach 进入容器
* docker rm 删除容器

# Dockerfile
* FROM 
    就是指定基础镜像，因此一个 Dockerfile 中 FROM 是必备的指令，并且必须是第一条指令。
  > FROM scratch:
    如果你以 scratch 为基础镜像的话，意味着你不以任何镜像为基础，接下来所写的指令将作为镜像第一层开始存在。

* RUN 
    指令是用来执行命令行命令的。一个run会生成一层镜像
* COPY 
    COPY <源路径>... <目标路径>
    COPY 指令将从构建上下文目录中 <源路径>的文件/目录复制到新的一层的镜像内的 <目标路径> 位置。
* ADD
    高级复制，最好用场景为复制并自动解压
* WORKDIR 
    工作路径
* docker build
    构建镜像,docker build -t zheng:v1 .

# docker 命令补全
使用时发现默认的docker命令没有补全功能，输入一些容器id时很麻烦，所以对zsh做一些升级
* 下载补全脚本
`mkdir -p ~/.zsh/completion`
`curl -L https://raw.githubusercontent.com/docker/docker/master/contrib/completion/zsh/_docker > ~/.zsh/completion/_docker`
`curl -L https://raw.githubusercontent.com/docker/compose/master/contrib/completion/zsh/_docker-compose > ~/.zsh/completion/_docker-compose`
* 配置 ~/.zshrc, 主要添加或修改下面两行
`fpath=(~/.zsh/completion $fpath)`
`autoload -Uz compinit && compinit -u`
* 重启shell
`exec $SHELL -l`

# docker-compose