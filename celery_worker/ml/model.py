import os
from transformers import T5ForConditionalGeneration, AutoTokenizer

MODEL_PATH = os.environ['MODEL_PATH']
MAX_TARGET_LENGTH = int(os.environ['MAX_TARGET_LENGTH'])
MAX_SOURCE_LENGTH = int(os.environ['MAX_SOURCE_LENGTH'])
DEVICE = os.environ['DEVICE']
TASK_PREFIX = os.environ['TASK_PREFIX']


class T5Model:
    """ Wrapper for loading and serving pre-trained model"""

    def __init__(self):
        self.model, self.tokenizer = self._load_model_from_path(MODEL_PATH)

    @staticmethod
    def _load_model_from_path(path):
        model = T5ForConditionalGeneration.from_pretrained(path, local_files_only=True).to(DEVICE)
        tokenizer = AutoTokenizer.from_pretrained(path, local_files_only=True)
        return model, tokenizer

    @staticmethod
    def _process_output(text):
        return text

    def generate(self, text):
        encoding = self.tokenizer(
            f'{TASK_PREFIX}: {text}',
            padding="max_length",
            max_length=MAX_SOURCE_LENGTH,
            truncation=True,
            return_tensors="pt",
        )
        out = self.model.generate(input_ids=encoding['input_ids'].to(DEVICE), max_length=MAX_TARGET_LENGTH)
        summary = self.tokenizer.batch_decode(out, skip_special_tokens=True)[0]
        proc_summary = self._process_output(summary)
        return proc_summary
