FROM ubuntu:20.04
WORKDIR /usr/src/app
ENV TZ=Europe/Paris

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install python3-pip ffmpeg -y

COPY ./Project_data/* ./Project_data/
COPY ./Api/requirements.txt .
RUN pip install -r requirements.txt
COPY ./Api .

EXPOSE 3000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]