# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /home/data
COPY proj2docker.py ./
COPY IF.txt ./
COPY Limerick.txt ./
COPY result.txt ./

CMD ["python", "proj2docker.py"]
