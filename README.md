# Openstack
[![Build Status](https://travis-ci.org/AUCR/openstack.svg?branch=master)](https://travis-ci.org/AUCR/openstack)
[![codecov](https://codecov.io/gh/AUCR/openstack/branch/master/graph/badge.svg)](https://codecov.io/gh/AUCR/openstack)
[![Coverage Status](https://coveralls.io/repos/github/AUCR/openstack/badge.svg)](https://coveralls.io/github/AUCR/openstack)

A Openstack plugin for AUCR


## Organization Support Slack
[![AUCR Slack](https://slack.aucr.io/badge.svg)](https://slack.aucr.io/)

Please contact us in the organization slack and join the Openstack room to ask any questions!


## How to install

From the AUCR/app/plugins dir just git clone https://github.com/AUCR/openstack and run the flask app.

    git clone https://github.com/AUCR/AUCR
    cd AUCR/app/plugins
    git clone https://github.com/AUCR/openstack
    cd ../..
    export FLASK_APP=aucr.py
    flask run --host=127.0.0.1
