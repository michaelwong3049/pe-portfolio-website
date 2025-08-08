#!/bin/bash

source env/bin/activate
systemctl daemon-reload
systemctl start myportfolio
docker compose -f docker-compose.prod.yml up -d --build

