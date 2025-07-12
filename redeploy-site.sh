#!/bin/bash

source env/bin/activate
systemctl daemon-reload
systemctl start myportfolio

