pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('clone') {
            steps {
             echo 'clone core test project'          
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