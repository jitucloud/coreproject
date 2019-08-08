### Jenkins in Docker
#### run jenkins in docker from docker hub
> docker run -d -p 8080:8080 -p 50000:50000 -v c:/workspace/personal/code/coreprojectvolume:/var/jenkins_home jenkins/jenkins

#### build docker image from Dockerfile
 > docker build -t demojenkins .
#### run jenkins in docker with above image and local volume
 > docker run -d -p 8080:8080 -p 50000:50000 -v c:/workspace/personal/code/coreprojectvolume:/var/jenkins_home demojenkins 

### Python demo app and demo unittest sample
#### run apptype1 unit test cases
 > python -m unittest discover -s tests/apptype1
#### run apptype1 and unit test and reports
 > python -m xmlrunner discover -s tests/apptype1 -o junit-reports
