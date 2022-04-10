#!/bin/bash
yum update -y
cd /home/ec2-user/invest-guide
git pull origin master
cd scripts
pip3 install --upgrade -r requirements.txt