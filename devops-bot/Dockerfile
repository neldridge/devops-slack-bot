FROM phusion/baseimage:latest
MAINTAINER Nick Eldridge <nicholas.eldridge@gmail.com>


CMD ["/sbin/my_init"]


RUN apt-get update && apt-get -y install python python-pip

RUN pip install slackbot
RUN pip install logging
#RUN pip install re

RUN mkdir -p /devops-bot
COPY app/ /devops-bot

RUN mkdir -p /etc/service/devops-bot/
COPY devops-bot.sh /etc/service/devops-bot/run
RUN chmod +x /etc/service/devops-bot/run

# Clean up APT.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
