pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('prepration') {
           environment {
               apptype = 'apptype1'
               appname = 'appname1'
           }
          steps {
             echo 'figure out the apptype and appname using some grovy'  
             print(env.apptype)
             print(env.appname)

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