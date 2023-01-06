FROM hitokizzy/ibel:slim-buster

RUN git clone -b main https://github.com/ArmanGG01/PyroKar2-Userbot /home/PyroKar/
WORKDIR /home/PyroKar

CMD ["python3","-m","PyroKar"]
