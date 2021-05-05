# image: nowthatsdamp/homework07

FROM python:3.9
RUN apt-get update && apt-get install -y vim

RUN pip install flask redis hotqueue ipython
RUN mkdir /app

COPY ./source/* /

ENTRYPOINT ["python"]

