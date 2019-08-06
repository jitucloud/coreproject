def apptype = "apptype1"
def appname = "appname1"

pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('prepration') {
           agent { label 'master'}
           environment {
               JENKINS_PATH = sh(script: 'pwd', , returnStdout: true).trim()
           }
            steps {
             echo 'figure out ${apptype} and ${appname1} using grovy script'  
          }
        }
        stage('clone') {
            steps {
             echo 'figure out ${apptype} and ${appname1} using grovy script'  
          }
        }
        stage('test'){
            steps {
             echo 'clone generic unit test project'
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
          }
        }
    }
}