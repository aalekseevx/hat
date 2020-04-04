FROM node:12-alpine AS builder
WORKDIR /usr/src/frontend
COPY package.json ./
RUN npm install
COPY . .
RUN npm run production
RUN ls -la dist
