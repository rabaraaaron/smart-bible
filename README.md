# Smart Bible
This is the backend for the smart bible application. The purpose of this app is to provide ChatGPT-like responses to questions regarding the Bible, and argumentative information involving the Bible. This means that you should be able to ask this application anything about the Bible and it should be able to respond intelligently. This backend uses Python 3.11.5 as the primary language, FastAPI as the Rest framework, LlamaIndex as the data framework to work with LLMs, and 'insert vector DB here' as the vector database.

## How to Run Locally
- You will need to ensure that you are running Python 3.11.5 as the interpreter. You can check which interpreter you are running in VS Code by doing CTRL+SHFT+P. 
- You will need to install all the dependencies using pip in the requirements.txt. At the root you can run 'pip install -r src/requirements.txt'.
- You can then run 'uvicorn src.app:app --reload' or 'uvicorn src/app:app --reload' depending on which OS you are running.
- You should be able to hit your endpoint at 'http://localhost:8000' now.

## How to Run Using Docker
- Ensure you are able to run docker commands in your terminal/command prompt.
- Build the image by running 'docker build -t smart-bible .'
- Run a container from the image by running 'docker run -p 8000:8000 -v ./src/:/src/ smart-bible'
- You should be able to hit your endpoint at 'http://localhost:8000' now.

## Tips
- If you are running on Windows, you will need to run this application in Docker. Linux and Mac can run normally.
- Use Postman for hitting the API endpoints.
