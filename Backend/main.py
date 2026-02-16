# from fastapi import FastAPI
# from pydantic import BaseModel
# from model import recommend_schemes

# app = FastAPI(title="Bharat AI Saathi 🇮🇳")

# # User input structure
# class UserInput(BaseModel):
#     age: int
#     gender: str
#     income: int
#     state: str
#     category: str

# # Home route
# @app.get("/")
# def home():
#     return {"message": "Bharat AI Saathi Backend Running 🚀"}

# # Recommendation route
# @app.post("/recommend")
# def recommend(user: UserInput):

#     schemes = recommend_schemes(user.dict())

#     return {
#         "user_input": user,
#         "recommended_schemes": schemes
#     }



# from fastapi import FastAPI
# from pydantic import BaseModel
# from model import recommend_schemes

# # Create FastAPI app
# app = FastAPI(
#     title="Bharat AI Saathi 🇮🇳",
#     description="AI-powered Government Scheme Recommender",
#     version="1.0"
# )

# # User input model
# class UserInput(BaseModel):
#     age: int
#     gender: str
#     income: int
#     state: str
#     category: str


# # Home route
# @app.get("/")
# def home():
#     return {
#         "message": "Bharat AI Saathi Backend Running 🚀",
#         "status": "Success"
#     }


# # Recommendation route
# @app.post("/recommend")
# def recommend(user: UserInput):

#     recommendations = recommend_schemes(user.dict())

#     return {
#         "user_input": user,
#         "recommendations": recommendations
#     }


from fastapi import FastAPI
from pydantic import BaseModel
from model import recommend_schemes

app = FastAPI(
    title="Bharat AI Saathi 🇮🇳",
    description="AI-powered Government Scheme Recommender",
    version="1.0"
)

# User Input Schema
class UserInput(BaseModel):
    age: int
    gender: str
    income: int
    state: str
    category: str


# Home Route
@app.get("/")
def home():
    return {
        "message": "Bharat AI Saathi Backend Running 🚀"
    }


# Recommendation Route
@app.post("/recommend")
def recommend(user: UserInput):

    recommendations = recommend_schemes(user.dict())

    return {
        "user_profile": user,
        "recommendations": recommendations
    }
