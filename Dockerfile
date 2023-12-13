#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Lutpan-Userbot https://github.com/Lutpan-Userbot /home/Lutpanuserbot/ \
    && chmod 777 /home/Lutpanuserbot \
    && mkdir /home/Lutpanuserbot/bin/

COPY ./sample_config.env ./config.env* /home/Lutpanuserbot/

WORKDIR /home/Lutpanuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
