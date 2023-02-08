#! /bin/bash
celery -A shop worker -l info -n workerA.%h