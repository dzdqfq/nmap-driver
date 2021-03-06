FROM hub.sky-cloud.net/cicd/nmap-python:v2
MAINTAINER fangcong
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
WORKDIR /project/
ENV PATH=$PATH:/project
ENV PYTHONPATH /project
CMD ["python3","/nmap-driver/src/nmap_driver.py"]
