FROM public.ecr.aws/lambda/python:3.8

# EXPOSE 80
# EXPOSE 8080

ENV APP_HOME="./"
ENV PYTHONPATH=${APP_HOME}
ENV APP_WORKER_COUNT=1

ADD requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt  && \
	rm -rf /root/.cache/pip

COPY . ${APP_HOME}

# ENTRYPOINT ["/user/service/docker-entrypoint.sh"]
CMD ["app.main.handler"]
