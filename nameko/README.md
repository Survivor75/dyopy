## Nameko Microservices

Travel application designed in a microservice architecture.


## Running

`$ docker-compose up`


## Test

`curl -i -d "{\"airport\": \"first_airport\"}" localhost:8000/airport`

- response_1

`curl localhost:8000/airport/response_1`

- response_2

`curl -i -d "{\"airport\": \"second_airport\"}" localhost:8000/airport`

- response_3

`curl -i -d "{\"airport_from\": \"- response_1\", \"airport_to\": \"- response_3\"}" localhost:8000/trip`