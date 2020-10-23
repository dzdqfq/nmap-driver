FROM python:latest
WORKDIR /nmap-driver/
COPY . .
RUN mkdir /root/log
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y \
	nmap 
CMD ["python3","/nmap-driver/src/nmap-driver.py"]

