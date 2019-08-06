pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('clone') {
            steps {
             echo 'figure out appname and apptype using grovy script'  
             echo GIT_COMMIT %GIT_COMMIT% 
             echo 'clone core test project'          
          }
        }
        stage('test'){
             steps {
             echo 'clone unit test project'
             }
        }
        stage('run test'){
             steps {
             echo 'run test against the apptype and appname'
             }
        }
        stage('merge') {
            steps {
             echo 'merge feature to master'
        }}
    }
}