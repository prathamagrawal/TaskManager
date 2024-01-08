FROM node:alpine
WORKDIR /app
COPY . .
RUN npm install
ENV NODE_OPTIONS=--openssl-legacy-provider
# CMD ["npm", "run","build"]
