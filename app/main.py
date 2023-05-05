from transformers import T5ForConditionalGeneration, AutoTokenizer
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(
    title="Summarizing Model API",
    description="A simple API that use NLP model to summarize text",
    version="0.1",
)


# load the model
model = T5ForConditionalGeneration.from_pretrained('models/t5-base-jira-pubmed-finetuned', local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained('models/t5-base-jira-pubmed-finetuned', local_files_only=True)
MAX_SOURCE_LENGTH = 2048
MAX_TARGET_LENGTH = 256
DEVICE = 'cpu'


@app.get("/summarize")
def summarize(text: str):

    encoding = tokenizer(
        'summarize: ' + text,
        padding="max_length",
        max_length=MAX_SOURCE_LENGTH,
        truncation=True,
        return_tensors="pt",
    )
    out = model.generate(input_ids=encoding['input_ids'].to(DEVICE), max_length=MAX_TARGET_LENGTH)
    summary = tokenizer.batch_decode(out, skip_special_tokens=True)[0]

    # show results
    result = {"summary": summary}

    return result


