from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult

from celery_worker.tasks import generate_summary
from app.models import Task, Summary, Text
import uvicorn


app = FastAPI(
    title="Summarizing Model API",
    description="A simple API that use NLP model to summarize text",
    version="0.1",
    docs_url="/"
)


@app.post('/t5/summarize', response_model=Task, status_code=202)
async def summarization(text: Text):
    """Create celery generation task. Return task_id to client in order to retrieve result"""
    task_id = generate_summary.apply_async(args=[dict(text)], queue='PendingMeetingQueue')
    return {'task_id': str(task_id), 'status': 'Processing'}


@app.get('/t5/result/{task_id}', response_model=Summary, status_code=200,
         responses={202: {'model': Task, 'description': 'Accepted: Not Ready'}})
async def summarization_result(task_id):
    """Fetch result for given task_id"""
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': str(task_id), 'status': 'Success', 'summary': str(result)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
