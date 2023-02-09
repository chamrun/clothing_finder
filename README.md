# Clothing Finder

![screenshot](/screencapture.png)

A web system that crawls and displays clothing products. The system is composed of the following parts:

- A database (elasticsearch) to store the crawled data and keep it updated.
- A backend system that performs the following tasks:
    - Crawls products using python. New products are added and existing products in the database are updated.
    - Interacts between the frontend and the database using flask.
- A frontend system that consists of a Product Listing Page, displaying the products as follows:


## Getting Started


First, install elasticsearch:

[How to Install and Configure Elasticsearch on Ubuntu?](https://www.geeksforgeeks.org/how-to-install-and-configure-elasticsearch-on-ubuntu/)


Run the following commands to create docker image and run the container:

    $ docker build -t clothing_finder_ui ./crawler
    $ docker run --network host clothing_finder_crawler

    $ docker build -t clothing_finder_ui ./service
    $ docker run -p 5000:5000 --network host clothing_finder_service

    $ docker build -t clothing_finder_ui ./ui/ReactFakeShop
    $ docker run -p 3000:3000 --network host clothing_finder_ui


## Built With

- Flask for the webservice
- React for the UI
- Python for the crawler

