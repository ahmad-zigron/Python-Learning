pipeline{
  agent any
  parameters {
    string(name: 'host_param', 
      defaultValue: 'develop',
      description: 'Parameters for BlueOcean Pipeline')
  }
  stages {
    stage ('Example') {
      steps {
        echo'Hellow World of parameters'
        echo "Trying: ${params.host_param}"
      }
    }
  }
}
