#!/bin/bash

3.6venv
python main.py server &

ssh cds-pi-1 "3.6venv; cd ~/de-r-pi-cluster; python main.py localhost:8765" &
ssh cds-pi-2 "3.6venv; cd ~/de-r-pi-cluster; python main.py localhost:8765" &
ssh cds-pi-3 "3.6venv; cd ~/de-r-pi-cluster; python main.py localhost:8765" &

fg