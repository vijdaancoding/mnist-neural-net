# mnist-neural-net
This is a practice repository solely made for having fun with PDB, GitBash and Docker. 

The documentations of the process that took place when implementing each of these is located here:
1. [PDB](#pdb)
2. [GitBash](#gitbash)
3. [Docker](#docker)


## PDB

### Debugging and Deployment
The application includes a debugging breakpoint using the pdb module, allowing for easy debugging and troubleshooting. The application is designed to be deployed as a web application, making it accessible and user-friendly for a wide range of users. Overall, the MNIST digit recognition application demonstrates the effective deployment of machine learning models using Streamlit and TensorFlow.


We have the module pdb from python to set a break-point where might exist an error. Here is the screenshot of the breakpoint:



![image](https://github.com/vijdaancoding/mnist-neural-net/assets/125562989/9c0af30f-8eb4-40c9-b297-4b3872193143)

After we set the breakpoint our program flow stops at the break-point and we can easily debug the issues, here we have find the potential issue and fixed it i.e returning the digit as integar , it was returned as string before we debugged the code. Here see in the terminal:
The application includes a debugging breakpoint using the pdb module, allowing for easy debugging and troubleshooting. The application is designed to be deployed as a web application, making it accessible and user-friendly for a wide range of users. Overall, the MNIST digit recognition application demonstrates the effective deployment of machine learning models using Streamlit and TensorFlow.


We have the module pdb from python to set a break-point where might exist an error. Here is the screenshot of the breakpoint:


![image](https://github.com/vijdaancoding/mnist-neural-net/assets/125562989/9c0af30f-8eb4-40c9-b297-4b3872193143)


After we set the breakpoint our program flow stops at the break-point and we can easily debug the issues, here we have find the potential issue and fixed it i.e returning the digit as integar , it was returned as string before we debugged the code. Here see in the terminal:



![image](https://github.com/vijdaancoding/mnist-neural-net/assets/125562989/90200c04-5893-4796-af96-09c28208c122)


After we fix our issue we simply write the command continue in the terminal as shown:


![image](https://github.com/vijdaancoding/mnist-neural-net/assets/125562989/3a012c99-b55b-4bdc-af87-03c706ee6d10)



## GitBash

### Initialization 
A git repository was supposed to be initialized at our local setup. The git repo initially had all related files untracked. We used linux commands to add the files to our repo

![git ss 1](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/2b004977-ef26-4fc0-9d38-73ce1a75e896)

### Branch Creation
After working on our code in the master branch we came at an empasse and were forced to tune the hyperparameteres of our model as it was overfitting. We made a new branch called 'bugfix' 

![git ss 2](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/0dd134ee-4457-4852-86fc-f538051f6267)

### Merging Branches
After fixing the issue we merged the 'bugfix' branch back to our main branch. 

![git ss 3](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/d40c2ff6-ee93-4041-8190-906f4b69b982)

### Pushing to Hub
When satisfied with our current code and setup we pushed our code from our local repository to GitHub. 

![git ss 4](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/77c0000f-09ab-44f7-942f-bc032e40cb0d)

### Git Log
The following is a graphical representation of the git log

![image](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/ed414edd-418b-48e3-b44f-c6b5484cad69)


## Docker

### Docker File
To create a Docker container and push it to hub we first created a Dockerfile in VSCode 

![docker ss 1](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/5f4c6cc4-41ba-450f-b87c-13b958d5fb22)

### Requirements File
The docker container also includes all the required libraries that go into making your code run hence a requirements.txt file is necessary. 

![docker ss 2](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/c16ce79c-8256-4df2-ad1a-49e887b7c02d)

### Creating the Docker Container
Through the docker build command in vscode we were able to make a docker container on our local device. Then we uploaded the container on the DockerHub via Docker Desktop. To veiw the contianer on the Hub click [here](https://hub.docker.com/repository/docker/vijdaancoding/mnist-streamlit/general)

![docker ss 3](https://github.com/vijdaancoding/mnist-neural-net/assets/131896316/9b2f9ac9-3c2c-4eb5-9877-0ff3e1920ea7)

### Running the docker container from Docker hub on a local PC


![image (2)](https://github.com/vijdaancoding/mnist-neural-net/assets/125562989/35d57cdc-91dd-445d-ae2e-5ac66b5f9abe)


Here you can see our application is up and running 

![image (3)](https://github.com/vijdaancoding/mnist-neural-net/assets/125562989/a9d6360c-ff83-48bd-9079-502a8cb7c71a)






