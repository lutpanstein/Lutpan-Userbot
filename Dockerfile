#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Lutpan-Userbot https://github.com/Lutpan-Userbot /home/Lutpan-Userbot/ \
    && chmod 777 /home/Lutpan-Userbot \
    && mkdir /home/Lutpan-Userbot/bin/

COPY ./sample_config.env ./config.env* /home/Lutpan-Userbot/

WORKDIR /home/Lutpan-Userbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
