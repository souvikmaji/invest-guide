sam build --use-container --parallel --cached \
 --build-image StartEC2Instances=721790918739.dkr.ecr.ap-south-1.amazonaws.com/scheduler-lambda:latest \
 --build-image StopEC2Instances=721790918739.dkr.ecr.ap-south-1.amazonaws.com/scheduler-lambda:latest &&
sam deploy 