# ML Model Microservice
## Random Forest Deployment

Deploy the application to a VM
Steps:
* Clone the repository
```
git clone https://github.com/gziz/API-RF.git .
```
* Manually add the env file

* Build the docker file
```
docker build  -t <img-name> -f Dockerfile .
```

* Deploy
```
docker run --restart always -e PORT=8000 -p 80:8000 -d <img-name>
```
