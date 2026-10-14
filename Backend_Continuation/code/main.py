from fastapi import FastAPI
from auth import router as auth_router
from books import router as books_router

app = FastAPI(title="Library Management API")

app.include_router(auth_router)
app.include_router(books_router)
