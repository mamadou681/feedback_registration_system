import fastapi as _fastapi
import sqlalchemy.orm as _orm
import uvicorn

import services as _services
from forward_to_db import fetch_from_rabbitmq

# Create the table
_services.add_table()
# Create the object
app = _fastapi.FastAPI()


@app.get("/")
async def root():
    return {"ready": "to fecth data from rabbitmq and send it to db. Please go to /fetchdata "}


@app.get("/fetchdata")
async def create_userinfo(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await fetch_from_rabbitmq(db)


if __name__ == "__main__":

    uvicorn.run("main:app", port=5002, host="0.0.0.0", reload=True)
