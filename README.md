# GRPC Client - Server

- This work is part of `Interview` Task.


## Getting started

- This repository particularly consists the following:
    - `gRPC Server` which will have a simple api that will store the given data in a log file.
    - `gRPC Client` consists of a flask-webGUI where the data can be sent through a web interface via gRPC-client
- These instructions will get you to set up on your local machine for development and testing purposes.


## Pre-requisites

* Software:
  - Docker
  - Git
* Docker, gRPC, python, Flask, Vanilla html/Js/Css knowledge would be helpful to have.


## Installing

* Clone the repository or download and unzip it.    
* Build the docker image, do this in the project folder console.
   ```
    docker compose build
  ```
* Spin/Start the docker container, do this in the project folder console.
   ```
    docker compose up
  ```

## Usage

* Navigate to `http://localhost:4251/` for using the web-GUI.