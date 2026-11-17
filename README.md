# Streamlit Cohere Chatbot

## Project layout

- `app.py` is the Streamlit entry point.
- `chatbot/config.py` loads `COHERE_API_KEY` from the project-root `.env`.
- `chatbot/service.py` sends the conversation to Cohere.
- `.env.example` is a safe template; put your real key in `.env`, never in this file.
- `requirements.txt` lists the Python dependencies.

## Run on Windows

Open PowerShell in the folder containing `app.py`, then run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

In Notepad, replace the example value with your Cohere key, keeping this format:

```text
COHERE_API_KEY=your_actual_cohere_api_key
```

Save `.env`, close Notepad, and start the chatbot:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The `.env` file belongs in the same folder as `app.py`, not inside the virtual
environment. For compatibility, the app temporarily reads the older
`AI_Chatbot\venv\.env` location if the project-root `.env` does not exist and
displays a warning. Move the key to the project-root `.env` and remove the old
copy after confirming it works. The app still allows you to type a question if
the key is missing, but it cannot request an answer until a key is configured.
