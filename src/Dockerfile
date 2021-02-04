#Linux image I will be using
FROM alpine
WORKDIR /root/hello-world
COPY Printer.java /root/hello-world

#Install JDK start with run command
RUN apk add openjdk8
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

#compile
RUN javac Printer.java

ENTRYPOINT java Printer
