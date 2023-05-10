import importlib
from celery import Task

from celery_worker.worker import celery_app
import logging
logger = logging.getLogger(__name__)

class GenerateTask(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """
    abstract = True

    def __init__(self):
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        logger.info('Check Model...')
        if not self.model:
            logger.info('Loading Model...')
            module_import = importlib.import_module(self.path[0])
            model_obj = getattr(module_import, self.path[1])
            self.model = model_obj()
            logger.info('Model loaded')
        return self.run(*args, **kwargs)


@celery_app.task(ignore_result=False,
                 bind=True,
                 base=GenerateTask,
                 path=('celery_worker.ml.model', 'T5Model'),
                 )
def generate_summary(self, text):
    """
    Essentially the run method of GenerateTask
    """
    logger.info("Starting task...")
    summary = self.model.generate(text['text'])
    return summary
