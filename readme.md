# Groq Example - FastAPI Application

This project is a FastAPI application that integrates with an LLM client (Groq). Below are instructions to install, configure, and run the project.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Setting Up the .env File

To configure API keys and other sensitive data, create a `.env` file in the root directory:

```
API_KEY=<your-api-key>
```


Make sure to replace `<your-api-key>` with your actual API key for the LLM.

## Running the Groq Example

To run the example using the Groq LLM client, execute:

```bash
python -m app.llm.run_groq_example
```

This script loads the groq_poem.json prompt and interacts with the LLM to generate a poem based on the input.


## Running the Server

You can start the FastAPI server using uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 80 --reload
```

The app will be available at <http://localhost:80>. Swagger UI can be accessed at <http://localhost:80/docs>.

## Router Explanation

The llm router is located in `app/routes/llm.py`. This router defines an endpoint that interacts with the Groq LLM to generate poems.

## LLM Router

The router defines a GET route at `/llm/groq/poem/{country}`. This route reads a JSON file containing prompt messages, replaces the `{country}` placeholder with the provided country value, and generates a poem using Groq's LLM.
