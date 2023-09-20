
node('Linux'){
stage('Checkout'){
checkout scm}
stage('Unit Tests'){
    def imageName = 'helloworld'
    def workspace = pwd()
    echo "current workspace ${workspace}"
    sh "docker build -t ${imageName}-test -f Dockerfile.test ."
    sh "docker run --rm ${imageName}-test"
}
}
