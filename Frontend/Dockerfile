# Build Stage
FROM node:22 AS build

WORKDIR /app

# Install dependencies first
COPY package*.json ./
RUN npm install

# Then copy rest of the app
COPY . .

RUN npm run build

# Serve stage
FROM nginx:alpine

# Copy the built app to Nginx's HTML directory
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
