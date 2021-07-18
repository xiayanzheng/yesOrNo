FROM python:3.9
LABEL maintainer="xiayanheng@outlook.com"
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
ADD . /app
RUN pip3 install -r /app/requirements.txt
WORKDIR /app/be
EXPOSE 5000
CMD ["python3","app.py"]