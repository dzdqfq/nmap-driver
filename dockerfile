FROM python:latest
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y \
	nmap 
WORKDIR /project/
ENV PATH=$PATH:/project
ENV PYTHONPATH /project
CMD ["python3","/src/nmap-driver.py"]

