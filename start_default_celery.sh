#! /bin/bash
celery -A shop worker -l info -n workerA.%h -Q default,priority_tasks -c 4