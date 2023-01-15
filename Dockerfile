FROM hitokizzy/ibel:slim-buster

RUN git clone -b main https://github.com/ArmanGG01/PyroKar2-Userbot /home/PyroKar/
RUN pip3 install --upgrade pip setuptools 
RUN pip3 install -r https://raw.githubusercontent.com/ArmanGG01/PyroKar2-Userbot/main/requirements.txt

WORKDIR /home/PyroKar

CMD ["python3","-m","PyroKar"]
