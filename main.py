from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from pickle import dump

app = FastAPI()
nombreArchivo = "ClasificadorTweets.pkl"
modeloCargado = pickle.load(open(nombreArchivo, "rb"))

ClasificadorTweets, Tfidf_vect = modeloCargado


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Tweet(BaseModel):
    entrada: str


@app.post("/clasification/")
async def create_item(tweet: Tweet):
    prediccionEjemplo = Tfidf_vect.transform([tweet.entrada])
    resultadoPorcentaje = ClasificadorTweets.predict_proba(prediccionEjemplo)
    print(resultadoPorcentaje)
    favor = resultadoPorcentaje[0][0]
    contra = resultadoPorcentaje[0][1]

    return {"mensaje": tweet.entrada, "A favor": favor, "En contra": contra}
