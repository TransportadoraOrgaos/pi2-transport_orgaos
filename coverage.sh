#!/bin/bash
coverage run manage.py test
coverage html
xdg-open .code_coverage/index.html
