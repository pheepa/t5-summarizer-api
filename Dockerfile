FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cpu

COPY ./app /code/app
COPY ./models /code/models

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]