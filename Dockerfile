FROM python:3.9

WORKDIR /app

RUN pip install numpy

COPY script.py /app

CMD ["python3", "script.py"]
