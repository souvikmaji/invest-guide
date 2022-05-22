FROM public.ecr.aws/lambda/python:3.9

# Copy function code
COPY scheduler_crons ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
RUN  pip3 install wheel
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# will get overwritten by template.yml
CMD [ "start.handler" ]