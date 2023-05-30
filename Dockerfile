FROM amazon/aws-lambda-python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY snowflake_integ.py ${LAMBDA_TASK_ROOT}

CMD [ "snowflake_integ.handler" ]