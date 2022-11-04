FROM python:3.9
WORKDIR /usr/app/src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "-u", "./main.py"]