from celery import task


@task
def priority_test():
    return ''
