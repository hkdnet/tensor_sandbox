eval "$(docker-machine env tensor)"
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
docker run -v ${script_dir}/src:/data/tensor/ -it b.gcr.io/tensorflow/tensorflow 
