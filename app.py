from fastapi import FastAPI, Response, status, Request
from fastapi.exceptions import RequestValidationError
from controller.student_controller import student_router;
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI();

@app.get("/")
def home(response: Response):
    response.status_code = 200;
    return {"message": "Welcome to the API for the AWS Project", "author": "Jesús Andrei Torres Landero" }

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

app.add_exception_handler(RequestValidationError, custom_validation_exception_handler)
app.include_router(student_router)