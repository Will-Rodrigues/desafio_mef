FROM python:3
COPY . /main.py
WORKDIR /main.py
CMD python main.py