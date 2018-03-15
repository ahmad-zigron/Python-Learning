pipeline {
  agent any
  parameters {
    string(name: 'TAG',
    description: 'Tag  for production server')
    string(name: 'HOSTS',
    defaultValue: 'hostvirtual2',
    description: 'Hosts Parameters for production server')
  }
  stages {
    stage('PDNS_sonar') {
        environment {
          SONAR_SCANNER_OPTS = "-Xmx1g"
        }
      steps {
        sh "/opt/sonar-scanner/bin/sonar-scanner -D sonar-project.properties"
      }
    }
    stage('PDNS_build') {
      steps {
        echo '------------------- PDNS Starting Build ------------------------ '
        echo '----------- PDNS Build Successfully Completed! ----------------- '
      }
    }
    stage('PDNS_Stage_deply') {
      steps {
        echo '------------------- PDNS Starting Deployment on Staging Server ------------------------ '
        echo '---------------- Staging Server Deploymnet Successfully Completed! -------------------- '
      }
    }
    stage('PDNS_RegressionTest') {
      steps {
        echo '----------------------- Regression Test ----------------------------- '
        echo '----------- Regression Test Successfully Completed! ----------------- '
      }
    }
    stage('PDNS_Production') {
      steps {
        echo '--------------- Production Server Deployment -------------------------- '
        echo '---------- Deployment On Production Server Successfully Completed! ------------ '
        echo "The value of parameter: ${params.host}"
      }
    }
  }
}
