from shop.celery import app


@app.task
def priority_test():
    return ''
