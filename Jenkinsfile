pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build this'
        git(url: 'https://github.com/ahmad-zigron/Python-Learning.git', branch: 'master')
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deplyed project'
      }
    }
  }
}