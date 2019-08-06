pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('clone') {
            steps {
             echo 'clone core project'
             git url: 'https://github.com/jitucloud/coreproject.git'
          }
        }
        stage('test'){
             steps {
             echo 'clone unit test project'
             }
        }
        stage('merge') {
            steps {
             echo 'merge feature to master'
        }}
    }
}