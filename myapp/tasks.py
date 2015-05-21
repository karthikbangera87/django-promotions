from celery import task

# to perform a simple add task
@task()
def add(x,y):
   return x+y


