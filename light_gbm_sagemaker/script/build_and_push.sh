ACCOUNT_ID=$1
REGION=$2
REPO_NAME=$3

docker build -f ../docker/dockerfile-cli -t $REPO_NAME ../docker

docker tag $REPO_NAME $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest


aws ecr describe-repositories --repository-names "${REPO_NAME}" > /dev/null 2>&1

if [ $? -ne 0 ]
then
    aws ecr create-repository --repository-name "${REPO_NAME}" > /dev/null
fi

# Get the login command from ECR and execute it directly
$(aws ecr get-login --region ${REGION} --no-include-email)

# Get the login command from ECR in order to pull down the SageMaker PyTorch image
$(aws ecr get-login --registry-ids 763104351884 --region ${REGION} --no-include-email)



docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest

