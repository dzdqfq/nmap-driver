pipeline {
  agent {
    node {
      label 'master'
    }
  }
  parameters {
    string(name: 'distName', defaultValue: 'nmap-driver' , description: '镜像名')
    string(name: 'distRepository', defaultValue: 'http://mvn.sky-cloud.net:8081/repository/sky-statics/nmap-driver/', description: '静态文件发布位置')
  }
  stages {
    stage('build-dockerimage') {
      steps {
        script {
		  def GIT_COMMIT_HASH = sh (script: "git rev-parse --short HEAD", returnStdout: true).trim()
          def filter = sh(returnStdout: true, script: "expr substr $BRANCH_NAME 1 7").trim()
          if (filter != 'release' && filter != 'develop' && filter != 'test') {
                currentBuild.result = 'SUCCESS'
                return
          }
		  sh 'echo ${GIT_COMMIT_HASH}'
		  sh "git rev-parse --short HEAD"
          def distNumber = sh(returnStdout: true, script: "echo $BRANCH_NAME | sed \"s/.*\\///g\"").trim()
          def IMAGE_NAME = "${params.distName}:${distNumber}_build-${BUILD_NUMBER}"
          def PACKAGE_HOME = "${params.distRepository}${params.distName}.${distNumber}_build-${GIT_COMMIT_HASH}"
          sh "docker login -u docker-image-builder -p sky-cloud@SZ2018 hub.sky-cloud.net ; docker build -t hub.sky-cloud.net/sky/${IMAGE_NAME} . ; docker push hub.sky-cloud.net/sky/${IMAGE_NAME}"
          if (env.BRANCH_NAME == 'release/1.0.0') {
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.30.53 \"kubectl set image deploy/nmap-driver nmap-driver=hub.sky-cloud.net/sky/${IMAGE_NAME} -n sky\""
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.30.53 \"sed -i 's/nmap-driver:.*/${IMAGE_NAME}/g' /srv/sky/nmap-driver/nmap-driver.yaml\""
          }
          if (env.BRANCH_NAME == 'test') {
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.30.52 \"kubectl set image deploy/nmap-driver nmap-driver=hub.sky-cloud.net/sky/${IMAGE_NAME} -n sky\""
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.30.52 \"sed -i 's/nmap-driver:.*/${IMAGE_NAME}/g' /srv/sky/nmap-driver/nmap-driver.yaml\""
          }
          if (env.BRANCH_NAME == 'develop') {
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.30.51 \"kubectl set image deploy/nmap-driver nmap-driver=hub.sky-cloud.net/sky/${IMAGE_NAME} -n sky\""
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.30.51 \"sed -i 's/nmap-driver:.*/${IMAGE_NAME}/g' /srv/sky/nmap-driver/nmap-driver.yaml\""
          }
        }
      }
    }
  }
}
