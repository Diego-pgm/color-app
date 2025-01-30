pipeline {
    agent any
    stages {
        stage('Build image'){
            steps{
                sh 'docker build -t diegopgm23/color-app:prod .'
            }
        }
        stage('Push Image'){
            steps{
                sh 'docker push diegopgm23/color-app:prod'
            }
        }
        stage('Deploy image'){
            steps{
                sh 'ssh vagrant@192.168.0.62 docker run -dti --name color-app -p80:8080 -e APP_COLOR=lightgreen diegopgm23/color-app:dev'
            }
        }
    }
}