from djcelery import celery
from fabric.api import execute


def string_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

@celery.task()
def runFabricTask(module, task, host_string, *args,**kwargs):
    try:

       fabricTask=getattr(string_import(module), task)
       fabricTask.hosts=host_string
       result = execute(fabricTask, *args,**kwargs)
       if isinstance(result.get(host_string, None), BaseException):
          raise result.get(host_string)
    except Exception as e:
        print "my_celery_task -- %s" % e.message
    return result


