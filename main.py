from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)

@app.post("/paraphrase/")
async def paraphrase_text(original_text: str):
    # Here you would perform the paraphrasing logic using your desired method
    # For demonstration purposes, let's just return the original text
    return {"paraphrased_text": original_text}
