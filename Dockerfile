FROM ubuntu:20.04
# install openssh server
RUN apt update && \
    apt-get install -y sudo openssh-server python3 &&\
    apt-get clean

EXPOSE 22

# ssh welcome message setup
RUN chmod -x /etc/update-motd.d/*
COPY welcome_mesage.txt /etc/motd

# copy jail
COPY main.py /jail/jail.py
RUN chmod 555 /jail/jail.py

# make user
RUN useradd -u 1000 -m -s /jail/jail.py user && echo "user:password123" | chpasswd

# copy flag
COPY flag.txt /home/user/

# SSH config
RUN mkdir /var/run/sshd
RUN sed 's/#ClientAliveInterval/ClientAliveInterval 3600/' /etc/ssh/sshd_config && \
    sed 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config && \
    sed 's/PrintLastLog yes/PrintLastLog no/g' /etc/ssh/sshd_config && \
    mkdir -p /home/user/.cache && touch /home/user/.cache/motd.legal-displayed

CMD ["/usr/sbin/sshd","-D"]