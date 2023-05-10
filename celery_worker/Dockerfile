FROM python:3.9

WORKDIR /code

COPY ./celery_worker/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cpu

#COPY ./celery_worker/ml /code/ml
#COPY ./models /code/models
#COPY ./celery_worker/tasks.py ./celery_worker/worker.py /code/
