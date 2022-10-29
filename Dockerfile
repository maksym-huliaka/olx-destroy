#Labels as key value pair
#Deriving the latest base image
FROM python:3.8

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

RUN apt-get install chromium-chromedriver

# Set display port as an environment variable
ENV DISPLAY=:99

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "./source/main.py"]