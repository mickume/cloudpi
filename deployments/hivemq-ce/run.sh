
echo ""
echo "  HiveMQ Start Script for Linux/Unix v1.10"
echo ""

JAVA_OPTS="$JAVA_OPTS -Djava.net.preferIPv4Stack=true"
JAVA_OPTS="$JAVA_OPTS -noverify"

JAVA_OPTS="$JAVA_OPTS --add-opens java.base/java.lang=ALL-UNNAMED"
JAVA_OPTS="$JAVA_OPTS --add-opens java.base/java.nio=ALL-UNNAMED"
JAVA_OPTS="$JAVA_OPTS --add-opens java.base/sun.nio.ch=ALL-UNNAMED"
JAVA_OPTS="$JAVA_OPTS --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED"
JAVA_OPTS="$JAVA_OPTS --add-exports java.base/jdk.internal.misc=ALL-UNNAMED"
JAVA_OPTS="$JAVA_OPTS -Djava.security.egd=file:/dev/./urandom"
JAVA_OPTS="$JAVA_OPTS -XX:+CrashOnOutOfMemoryError"
# JMX Monitoring
# JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9010 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"
HOME_OPT="-Dhivemq.home=$HIVEMQ_FOLDER"

JAR_PATH="$HIVEMQ_FOLDER/bin/hivemq.jar"
exec "java" ${HOME_OPT} ${JAVA_OPTS} ${JAVA_EXTRA_OPTS} -jar ${JAR_PATH}
