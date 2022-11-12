from fastapi import FastAPI

app = FastAPI()


@app.post('/interactions')
async def post_interactions():
    ...  # TODO FastAPI POST endpoint
