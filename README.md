### start jenkins in docker with local volume
> docker run -d -p 8080:8080 -p 50000:50000 -v c:/workspace/personal/code/coreprojectvolume:/var/jenkins_home jenkins/jenkins

### run apptype1 unit test cases

> python -m unittest discover -s tests/apptype1
