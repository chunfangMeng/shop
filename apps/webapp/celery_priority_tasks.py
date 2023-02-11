from celery import task, shared_task


@task(name='priority_tasks')
def priority_test():
    return ''
