import asyncio
import os
import threading
import time
from pathlib import Path
from fastapi import FastAPI
import logging

from lit_generator import LitGenerator

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
model_name = "tiiuae/falcon-7b-instruct"

logger = logging.getLogger('LitGenerator')

app = FastAPI()
app.lock = False
lock = asyncio.Lock()

checkpoint_dir = Path('/home/mn/lit-gpt-api/checkpoints/tiiuae/falcon-7b-instruct')

generator = LitGenerator()
generator.setup(
    checkpoint_dir=checkpoint_dir
)

@app.get("/simple-query")
async def execute_query(query: str) -> list[str]:
    curr_thread = threading.current_thread()
    print(f"Running on thread: {curr_thread.ident}/{curr_thread.name} PID: {os.getpid()}")
    print(f'Query: {query}')

    async with lock:
        t1 = time.time()
        result = generator.query(
            prompt=query,
            top_k=500,
            temperature=0.1,
        )
        logger.info(f"Query finished in : {time.time() - t1:.02f} seconds.")
        print(f"Having result: {result}")

        return [result]
