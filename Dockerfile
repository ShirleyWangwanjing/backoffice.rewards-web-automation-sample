FROM       joyzoursky/python-chromedriver:3.7-selenium
RUN        pip install pipenv && pip install PyYAML && pip install Appium-Python-Client && pip install requests && pip install allure-behave && pip install cryptography && pip install pymssql && pip install Faker && pip install behave --no-cahce-dir
COPY       . /app
WORKDIR    /app
ENV        SHELL=/bin/bash
ENTRYPOINT ["pipenv", "run"]
CMD        ["python"]