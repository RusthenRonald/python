from exapi import FAstAPI
app=FAstAPI()
@app.get("/")
def read_root():
    return {"message":"olá,Mundo!"}