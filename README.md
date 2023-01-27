![screenshot](/screencapture.png)

First, install elasticsearch:

[How to Install and Configure Elasticsearch on Ubuntu ?](https://www.geeksforgeeks.org/how-to-install-and-configure-elasticsearch-on-ubuntu/)


Run the following commands to create docker image and run the container:

    $ docker build -t clothing_finder_ui ./crawler
    $ docker run --network host clothing_finder_crawler

    $ docker build -t clothing_finder_ui ./service
    $ docker run -p 5000:5000 --network host clothing_finder_service

    $ docker build -t clothing_finder_ui ./ui/ReactFakeShop
    $ docker run -p 3000:3000 --network host clothing_finder_ui
