FROM node:alpine
WORKDIR /usr/app
COPY package.json .
RUN npm install\
    && npm install typescript -g
COPY . .
RUN tsc
RUN export HOST="0.0.0.0"
CMD ["npm", "start"]