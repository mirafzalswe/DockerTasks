# before built image i  installed node version 11-alpine 

# # This Dockerfile starts by using the official Node.js 11 image based on Alpine Linux.
# FROM node:11-alpine

# # Copies the 'app.js' file from the local directory into the root directory of the container.
# COPY app.js .

# # Specifies the default command to run when the container starts.
# # It instructs the Node.js interpreter to execute the 'app.js' script within the container.
# CMD [ "node", "app.js" ]

FROM python:3.11-alpine
ENV first_name="Mirafzal"
ENV last_name="Bakhodirov"
ENV age="19"
WORKDIR /app
COPY main.py /app/
CMD ["python", "main.py"]




