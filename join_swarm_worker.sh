TOKEN=$(ssh cds-pi-1 "docker swarm join-token worker --quiet")
docker swarm join --token $TOKEN cds-pi-1:2377
