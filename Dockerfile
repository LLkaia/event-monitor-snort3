FROM kaiall/snort3:latest
WORKDIR /root/snort/

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./snort3_monitor ./snort3_monitor

COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT export SNORT_HOME_NET=$(ip addr show eth0 | grep 'inet ' | awk '{print $2}') && \
    sed -i "s#^HOME_NET =.*#HOME_NET = '$SNORT_HOME_NET'#" /usr/local/etc/snort/snort.lua && \
    /usr/bin/supervisord