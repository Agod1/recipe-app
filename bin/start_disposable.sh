#!/bin/bash

IMAGE_NAME="recipe-app"

# 'BASH_SOURCE[0]' gives the file path e.g. './bin/start_disposable.sh'
# 'dirname' then extracts the directory of the file e.g. './bin'
# 'cd' changes the directory to that of 'bin' e.g. 'cd ./bin'
# 'pwd' extracts the path of the current working directory e.g. '/Users/admin/triton/bin'
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 'dirname' then extracts the directory of the project e.g. '/Users/admin/triton/'
ROOT="$(dirname "${SCRIPT_DIR}")"

# First check if our image has been built. If not, build it.
if [[ "$(docker images -q ${IMAGE_NAME}:latest 2> /dev/null)" == "" ]]; then
    echo " ----- Recipe App Image Does Not Exist. Building Now. -----"
    docker build -t ${IMAGE_NAME} "${ROOT}"
else
    echo " ----- Recipe App Image Available for Use. -----"
fi

# Now, depending on whether our services are running or not, link them into our disposable container.
echo " ----- Run Recipe application Disposable Container -----"
docker run \
    -i \
    -t \
    -p 8000:8000 \
    ${IMAGE_NAME}

echo " ----- EXITED from disposable container -----"
echo " ----- Removing Exited Containers. -----"

# Now grep through all containers and stop those that have been "exited". Only do that for our service.
docker ps -a | grep Exited | awk '{ print $1,$2 }' | \
grep ${IMAGE_NAME} |  awk '{print $1 }' | xargs -I {} docker rm {}