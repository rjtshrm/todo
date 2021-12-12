FROM python:3.9

LABEL maintainer="rjt.rjtshrm94@gmail.com"

RUN apt update && apt install stress-ng -y

WORKDIR /home/app/TODO

COPY . .

#SHELL ["/bin/bash", "-c"] 
#RUN python -m pip install --user virtualenv
#RUN python -m venv pyenv && source pyenv/bin/activate

RUN pip install -r requirements.txt


ENV ALLOWED_HOSTS=127.0.0.1

EXPOSE 8000

#ENTRYPOINT ["gunicorn"]
#CMD ["TODO.wsgi:application", "--bind", "0.0.0.0:8000"]

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]








 