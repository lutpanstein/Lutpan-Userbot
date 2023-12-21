#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#
# Izzy Ganteng

FROM ayiinxd/ayiin:xd

RUN git clone -b Lutpanstein/Lutpan-Userbot https://github.com/Lutpanstein/Lutpan-Userbot /home//lutpanuserbot/ \
    && chmod 777 /home/lutpanuserbot \
    && mkdir /home/lutpanuserbot/bin/

#COPY ./sample.env ./.env* /home/lutpanuserbot/

WORKDIR /home/lutpanuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
