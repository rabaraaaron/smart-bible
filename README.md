# Smart Bible
This is the backend for the smart bible application. The purpose of this app is to provide ChatGPT-like responses to questions regarding the Bible, and argumentative information involving the Bible. This means that you should be able to ask this application anything about the Bible and it should be able to respond intelligently. 

## Technology Used
This backend uses Python 3.11.5 as the primary language, FastAPI as the Rest framework, LlamaIndex as the data framework to work with LLMs, Docker as the virtualization platform, and Elastic Search as the vector database.
<p align="center">
  <img src="images/fast-api.png" width="350" alt="accessibility text"> <br>
  <img src="images/docker.png" width="350" alt="accessibility text"> <br>
  <img src="images/python.png" width="350" title="hover text"> <br>
  <img src="images/llama-index.jpg" width="350" alt="accessibility text"> <br>
</p>

## How to Run
- Ensure you are able to run docker commands in your terminal/command prompt.
- Run 'docker compose up' at the root level of the project.
- You should be able to hit your endpoint at 'http://localhost:8000' now.

## Tips
- If you are running on Windows, you will need to run this application in Docker. Linux and Mac can run normally.
- Use Postman for hitting the API endpoints.
