pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build this'
        git(url: 'https://github.com/ahmad-zigron/Python-Learning/blob/master/Ahmad/Challange3/Q4.py', branch: 'master')
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deplyed project'
      }
    }
  }
}