def imageName = 'helloworld';
def workspace = pwd()
node('workers'){
stage('Checkout'){
checkout scm}
stage('Unit Tests'){
    echo "current workspace ${workspace}"
    sh "docker build -t ${imageName}-test -f Dockerfile.test"
    sh "docker run --rm ${imageName}-test"
}
}
