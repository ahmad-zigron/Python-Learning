pipeline{
  agent any
    parameters {
    string(name: 'host', 
    defaultValue: 'develop',
    description: 'Parameters for BlueOcean Pipeline')
  }
  stages{
    stage ('Example'){
      steps{
        echo'Hellow World of parameters'
        echo "Trying: ${params.host}"
      }
    }
  }
}
