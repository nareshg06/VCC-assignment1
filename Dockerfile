#To lockin with python version
FROM python:3.10.12
#To copy file from local to /app directory
COPY . /app
	
WORKDIR /app
	
RUN pip install -r requirements.txt
	
#run the command 
CMD ["Python", "app.py"]
