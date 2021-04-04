FROM python:3.7
# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y --only-upgrade && \
    apt-get install -y --no-install-recommends netcat

# Creation of the workdir
RUN mkdir /kartaca
WORKDIR /kartaca
# Add requirements.txt file to container
ADD requirements.txt /kartaca/
# Install requirements
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
# Add the current directory(the web folder) to Docker container
ADD . /kartaca/
COPY boot-strap.sh ./
RUN chmod +x /kartaca/boot-strap.sh
ENTRYPOINT ["sh","boot-strap.sh"]
