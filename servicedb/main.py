from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import uvicorn

from services import get_db, add_table
from forward_to_db import fetch_from_rabbitmq

# Create the table
add_table()
# Create the object
app = FastAPI()


@app.get("/")
async def root():
    return {"ready": "to fecth data from rabbitmq and send it to db. Please go to /fetchdata "}


@app.get("/fetchdata")
async def create_userinfo(db: Session = Depends(get_db)):
    return await fetch_from_rabbitmq(db)


if __name__ == "__main__":

    uvicorn.run("main:app", port=5002, host="0.0.0.0", reload=True)
