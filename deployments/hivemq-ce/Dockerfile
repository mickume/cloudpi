FROM registry.access.redhat.com/ubi8/ubi

EXPOSE 1883

ENV HIVEMQ_CE_VERSION=2019.1 \
    JAVA_OPTS="-XX:+UseNUMA" \
    APP_ROOT="/opt/app-root" 

# install basics and OpenJDK11
RUN set -x && yum install -y wget java-11-openjdk-devel.x86_64 unzip

# install HiveMQ
RUN wget -O ${APP_ROOT}/hivemq-${HIVEMQ_CE_VERSION}.zip https://github.com/hivemq/hivemq-community-edition/releases/download/${HIVEMQ_CE_VERSION}/hivemq-ce-${HIVEMQ_CE_VERSION}.zip \
    && unzip ${APP_ROOT}/hivemq-${HIVEMQ_CE_VERSION}.zip  -d ${APP_ROOT}\
    && rm -f ${APP_ROOT}/hivemq-${HIVEMQ_CE_VERSION}.zip \
    && mv ${APP_ROOT}/hivemq-ce-${HIVEMQ_CE_VERSION} ${APP_ROOT}/hivemq
    
# move the custom configuration files
COPY config.xml ${APP_ROOT}/hivemq/conf/config.xml
COPY logback.xml ${APP_ROOT}/hivemq/conf/logback.xml

# substitute eval for exec and replace OOM flag if necessary (for older releases). This is necessary for proper signal propagation
RUN sed -i -e 's|eval \\"java\\" "$HOME_OPT" "$JAVA_OPTS" -jar "$JAR_PATH"|exec "java" $HOME_OPT $JAVA_OPTS -jar "$JAR_PATH"|' ${APP_ROOT}/hivemq/bin/run.sh && \
    sed -i -e "s|-XX:OnOutOfMemoryError='sleep 5; kill -9 %p'|-XX:+CrashOnOutOfMemoryError|" ${APP_ROOT}/hivemq/bin/run.sh

# Make broker data persistent throughout stop/start cycles
#VOLUME /opt/hivemq/data

# Persist log data
#VOLUME /opt/hivemq/log

# drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:0 /opt && chmod -R ug+rwx /opt

WORKDIR ${APP_ROOT}/hivemq
USER 1001

CMD ["/opt/app-root/hivemq/bin/run.sh"]
