.ONESHELL:

make m4b-tool:
# clone m4b-tool repository
#git clone 
https://github.com/sandreas/m4b-tool.git
# change directory
cd m4b-tool
# build docker image - this will take a while
docker build . -t m4b-tool
# create an alias for m4b-tool running docker
alias m4b-tool='docker run -it --rm -u $(id 
-u):$(id -g) -v "$(pwd)":/mnt m4b-tool'
# testing the command
m4b-tool --version
