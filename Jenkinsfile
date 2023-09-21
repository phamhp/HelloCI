
node('Built-In Node'){
    try{
        stage('Checkout'){
            echo "Checking out ${branch}"

            try {
                checkout changelog: false, poll: false, scm: [
                    $class: 'GitSCM',
                    branches: [
                        [name: "*/${branch}"]
                    ],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [
                        [$class: 'CleanBeforeCheckout']
                    ],
                    submoduleCfg: [],
                    userRemoteConfigs: [
                        [url: 'ssh://git@github.com:phamhp/HelloCI.git']
                    ]
                ]
            } catch (error) {
                echo "Failed to checkout branch...retrying"
                retry(3) {
                    sleep 30
                    checkout changelog: false, poll: false, scm: [
                        $class: 'GitSCM',
                        branches: [
                            [name: "*/${branch}"]
                        ],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [
                            [$class: 'CleanBeforeCheckout']
                        ],
                        submoduleCfg: [],
                        userRemoteConfigs: [
                            [url: 'ssh://git@github.com:phamhp/HelloCI.git']
                        ]
                    ]
                }
            }
        
        
        
        
        }
        stage('Unit Tests'){
        def imageName = 'helloCI'
        def workspace = pwd()
        echo "current workspace ${workspace}"
        sh "docker build -t ${imageName}-test -f Dockerfile.test ."
        sh "docker run --rm ${imageName}-test"  
        }


    }catch(e){
        currentBuild.result = "FAILURE"
        throw e
    }

}
