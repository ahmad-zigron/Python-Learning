pipeline{
  agent any
  stages {
    stage ('Example') {
      input( message: 'What is Your Production Server ', ok: 'OK', parameters: [string(defaultValue: 'hostvirtula2', description: 'Production Host of Health Monitor ', name: 'HOST')])
      steps {
        echo'Hellow World of parameters'
        echo "Trying: ${params.HOST}"
      }
    }
  }
}
