FROM  python:2.7.15-stretch

RUN apt-get update

RUN pip install python-pushsafer

RUN pip install sense-hat

ADD sense.py   /sense/sense.py

WORKDIR /sense

CMD ["python", "/sense.py"]
