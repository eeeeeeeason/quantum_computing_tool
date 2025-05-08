# 使用官方 Python 3.9.12 镜像
FROM python:3.9.12-slim

# 设置工作目录
WORKDIR /app

# 安装依赖
RUN pip install --upgrade pip
# 安装cpu版本的pytorch,pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install torch==1.13.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install spinqit
RUN pip install flask -i https://mirrors.aliyun.com/pypi/simple/
# spinqit对应的版本可能没锁定numpy
RUN pip install numpy==1.23.0 -i https://mirrors.aliyun.com/pypi/simple/


# 启动一个终端，保持活跃、
CMD ["tail", "-f", "/dev/null"]


