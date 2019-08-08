FROM jenkins:alpine
USER root
RUN apk add --update python py-pip 
