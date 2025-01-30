pipeline {
    agent any
    stages {
        stage('Build image'){
            steps{
                sh 'docker build -t diegopgm23/color-app:dev .'
            }
        }
        stage('Push Image'){
            steps{
                sh 'docker push diegopgm23/color-app:dev'
            }
        }
        stage('Deploy image'){
            steps{
                sh 'ssh vagrant@192.168.0.60 docker run -dti --name color-app -p8080:8080 -e APP_COLOR=red diegopgm23/color-app:dev'
            }
        }
    }
}