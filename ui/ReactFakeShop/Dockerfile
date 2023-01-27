# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and yarn.lock to the container
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn

# Copy the rest of the application code to the container
COPY . .

# Build the app
RUN yarn build

# Specify the command to run when the container starts
CMD ["yarn", "start"]