FROM jenkins/jenkins:lts

# Install ngrok
USER root
RUN curl -L https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz -o ngrok.tgz && \
    tar -xzf ngrok.tgz && \
    mv ngrok /usr/local/bin/ && \
    rm ngrok.tgz
USER jenkins

# Create a startup script to run ngrok and Jenkins
USER root
RUN echo '#!/bin/bash\n\
ngrok authtoken 32MPylzVFD1zt9hHflx2uD8iN4V_72ZmiBG8r7HqGVDfJA8KG\n\
ngrok http 8080 &\n\
exec /usr/local/bin/jenkins.sh' > /usr/local/bin/start.sh && \
    chmod +x /usr/local/bin/start.sh
USER jenkins

# No Python installation needed - training runs in separate 'trainer' container