
from fastapi import FastAPI

klu = FastAPI(
    title="AI Tutor",
    description="AI Tutor PBL Project",
    version="1.0.0"
)

@klu.get("/")
def home():
    return {"message": "Welcome to AI Tutor Project"}


@klu.get("/demo")
def demo():
    return {"message": "KL University"}


@klu.get("/askquestion")
def ask():
    return {
        "message": "What is LLM",
        "Answer": "Large Language Model"
    }
@klu.get("/student")
def student():
    return {"id":1,"name" :"Ram", "gender":"male", "course":"DSA"}

@klu.get("/students")
def students():
    return [{"id":1,"name" :"Ram", "gender":"male", "course":"DSA"},
            {"id":2,"name" :"Aasritha","gender":"female", "course":"DSA"},
            {"id":3,"name" :"Namitha", "gender":"female", "course":"DSA"}]
