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
          def filter = sh(returnStdout: true, script: "expr substr $BRANCH_NAME 1 6").trim()
          if (filter == 'master') {
		      sh 'echo ${GIT_COMMIT_HASH}'
		      sh "git rev-parse --short HEAD"
              def distNumber = sh(returnStdout: true, script: "echo $BRANCH_NAME | sed \"s/.*\\///g\"").trim()
              def PACKAGE_HOME = "${params.distRepository}${params.distName}.${distNumber}_build-${GIT_COMMIT_HASH}"
              sh "docker login -u docker-image-builder -p sky-cloud@SZ2018 hub.sky-cloud.net ; docker build -t hub.sky-cloud.net/sky/${params.distName}:${distNumber}_build-${BUILD_NUMBER} . ; docker push hub.sky-cloud.net/sky/${params.distName}:${distNumber}_build-${BUILD_NUMBER}"  
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.1.146 \"docker pull hub.sky-cloud.net/sky/${params.distName}:${distNumber}_build-${BUILD_NUMBER} \""
              sh "sshpass -p r00tme ssh -o StrictHostKeyChecking=no root@192.168.1.146 \"kubectl set image deploy/nmap-driver nmap-driver=hub.sky-cloud.net/sky/${params.distName}:${distNumber}_build-${BUILD_NUMBER} -n sky\""

          }
        }
      }
    }
  }
}