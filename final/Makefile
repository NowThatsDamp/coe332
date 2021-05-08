NSPACE="mdo572"
APP="final"
VER="1.0"
RPORT="6404"
FPORT="5024"
UID="869715"
GID="816966"

list-targets:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'


build-db:
	docker build -t ${NSPACE}/${APP}-db:${VER} \
                     -f docker/Dockerfile.db \
                     ./

build-api:
	docker build -t ${NSPACE}/${APP}-api:${VER} \
                     -f docker/Dockerfile.api \
                     ./

build-wrk:
	docker build -t ${NSPACE}/${APP}-wrk:${VER} \
                     -f docker/Dockerfile.wrk \
                     ./


test-db: build-db
	docker run --name ${NSPACE}-db \
	               --rm \
				   -it \
                   --network ${NSPACE}-network-test \
				   -p ${RPORT}:6379 \
                   -u ${UID}:${GID} \
                   -v ${PWD}/data/:/data \
                   ${NSPACE}/${APP}-db:${VER}

test-api: build-api
	docker run --name ${NSPACE}-api \
	               --rm \
	               -it \
                   --network ${NSPACE}-network-test \
			       --env REDIS_IP=${NSPACE}-db \
                   -p ${FPORT}:5000 \
                   ${NSPACE}/${APP}-api:${VER} 

test-wrk: build-wrk
	docker run --name ${NSPACE}-wrk \
	               --rm \
				   -it \
                   --network ${NSPACE}-network-test \
                   --env REDIS_IP=${NSPACE}-db \
                   ${NSPACE}/${APP}-wrk:${VER} 


clean-db:
	docker ps -a | grep ${NSPACE}-db | awk '{print $$1}' | xargs docker rm -f

clean-api:
	docker ps -a | grep ${NSPACE}-api | awk '{print $$1}' | xargs docker rm -f

clean-wrk:
	docker ps -a | grep ${NSPACE}-wrk | awk '{print $$1}' | xargs docker rm -f



build-all: build-db build-api build-wrk

test-all: test-db test-api test-wrk

clean-all: clean-db clean-api clean-wrk



