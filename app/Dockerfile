FROM python:3.9

WORKDIR /code

COPY ./app/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /code/
#COPY ./app/main.py ./app/models.py /code/

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]