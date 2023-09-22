
node('MasterNode'){
    try{
        stage('Source'){
            echo "========================================================== git checkout =========================================================="
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
                        [url: 'https://github.com/phamhp/HelloCI.git']
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
                            [url: 'https://github.com/phamhp/HelloCI.git']
                        ]
                    ]
                }
            }
        echo "========================================================== Execute Jobs =========================================================="
        
        
        
        }
        stage('Unit Tests'){
            def imageName = 'hello_ci_unittest'
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
