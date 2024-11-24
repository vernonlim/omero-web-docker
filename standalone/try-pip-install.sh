#!/usr/bin/env bash

until /opt/omero/web/venv3/bin/pip install /sites/*
do
    echo "Retrying pip install"
done
