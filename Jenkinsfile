
node('Built-In Node'){
stage('Checkout'){
checkout scm}
stage('Unit Tests'){
    def imageName = 'helloCI'
    def workspace = pwd()
    echo "current workspace ${workspace}"
    sh "docker build -t ${imageName}-test -f Dockerfile.test ."
    sh "docker run --rm ${imageName}-test"
}
}
