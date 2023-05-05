# T5 base API for summarization

1. ``git clone https://huggingface.co/pheepa/t5-base-jira-pubmed-finetuned``
2. Create folder ``models`` and put ``t5-base-jira-pubmed-finetuned`` into this folder
3. ``docker build -t t5-base-sum .``
4. ``docker run -d -p 80:80 t5-base-sum``
5. Visit ``localhost:80/docs``
