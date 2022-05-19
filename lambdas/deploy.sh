sam package \
  --template-file template.yml \
  --output-template-file package.yml \
  --s3-bucket $S3_BUCKET

sam deploy \
  --template-file package.yml \
  --stack-name EC2SchedulerCron \
  --capabilities CAPABILITY_IAM