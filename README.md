# Question-Answering-System

### Description :

* <p align = "justify">Question Answering System using the BERT (Bidirectional Encoder Representations from Transformers) model is designed to understand and respond to natural language questions by extracting relevant information from a given context. BERT is a pre-trained language model that learns to understand the meaning of words and sentences by considering their surrounding context. The "Main" contains a python script that demonstrates how to create a Question Answering System using the Hugging Face Transformers library.</p>

* <p align = "justify">This system operates by tokenizing the question and context, encoding them using BERT to capture contextualized embeddings and incorporating the question into the context. By leveraging transformer layers, the model refines representations and predicts the start and end positions of the answer within the context. This enables the system to extract the answer and provide it in human-readable form.</p>

### FastAPI :

* <p align = "justify">The "main" contains a python script that demonstrates how to create a Question Answering API using FastAPI and the Hugging Face Transformers library. The API utilizes the BERT model pre-trained and fine-tuned on the SQuAD dataset (bert-large-uncased-whole-word-masking-finetuned-squad) to provide answers based on the given question and context.</p>

#### Requirements :

* Python
* Uvicorn
* FastAPI
* Transformers

#### Working :

* Make sure that Python 3.6 or above version is installed
* Install the necessary dependencies by running pip install fastapi uvicorn transformers
* Navigate to the respective directory and run the FastAPI server using "uvicorn main:app --reload"
* Access the Swagger UI at http://localhost:8000/docs to interact with the API
* Enter the question and context in the provided fields and click "Try it out" to get the predicted answer

### FastAPI In Docker :

* <p align = "justify">The "main" contains a python script that demonstrates how to create a Question Answering API using FastAPI and the Hugging Face Transformers library. The API utilizes the BERT model pre-trained and fine-tuned on the SQuAD dataset (bert-large-uncased-whole-word-masking-finetuned-squad) to provide answers based on the given question and context.</p>

#### Requirements :

* Python
* Torch
* Transformers
* FastAPI
* Pydantic
* Python-Multipart
* Uvicorn

#### Working :

* Create a Docker_File, Requirements.txt and main.py in the same directory as the code
* Build the Docker image using "docker build -t image_01 -f Docker_File ."
* Run the Docker container using "docker run image_01"
* The FastAPI application inside the Docker container will be accessible at http://localhost:80/answer
* Send POST requests with JSON data containing the question and context fields to get the corresponding answer
