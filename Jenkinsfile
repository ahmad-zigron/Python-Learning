pipeline {
  agent any
  stages {
    stage('sonar') {
      steps {
        git(url: 'https://ahmad-zigron@bitbucket.org/gaditek_dpi/automationscripts.git', branch: 'master')
      }
    }
    stage('build') {
      steps {
        sh './puredns_stag_build.sh'
      }
    }
    stage('stage-deploy') {
      steps {
        sh './puredns_stag_deploy.sh'
      }
    }
    stage('regression-test') {
      steps {
        sh '''cd automationscripts/test
        
./test_dnsperf.sh'''
      }
    }
    stage('pdns-prod') {
      steps {
        sh './puredns_prod.sh'
      }
    }
  }
}
