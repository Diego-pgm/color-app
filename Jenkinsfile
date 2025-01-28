pipeline {
    agent any
    stages {
        stage('Build image'){
            steps{
                sh 'docker build -t diegopgm23/color-app:file .'
            }
        }
        stage('Push Image'){
            steps{
                sh 'docker push diegopgm23/color-app:file'
            }
        }
    }
}