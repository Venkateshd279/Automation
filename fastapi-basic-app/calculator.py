from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Calculator API",
    description="Simple but powerful calculator API built with FastAPI",
    version="1.0"
)

class CalculationRequest(BaseModel):
    operand1: float
    operand2: float
    operation: str = Field(..., description="The operation to perform: add, subtract, multiply, divide")

class CalculationResponse(BaseModel):
    num1: float
    num2: float
    operation: str
    result: float
    message: str = "Calculation successful"

history = []

def perform_calculation(num1: float, num2: float, operation: str) -> float:
    operation = operation.lower()
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        return num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Supported: add, subtract, multiply, divide.")

@app.get("/", response_class=HTMLResponse)
def home():
    return """<h1>Calculator API</h1>
    <p>Welcome to the Calculator API!</p>"""

@app.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest):
    num1 = request.operand1
    num2 = request.operand2
    operation = request.operation.lower()
    result = perform_calculation(num1, num2, operation)
    history.append((num1, num2, operation, result))
    return CalculationResponse(num1=num1, num2=num2, operation=operation, result=result)

@app.post("/add", response_model=CalculationResponse)
def add(request: CalculationRequest):
    result = perform_calculation(request.operand1, request.operand2, "add")
    history.append((request.operand1, request.operand2, "add", result))
    return CalculationResponse(num1=request.operand1, num2=request.operand2, operation="add", result=result)

@app.post("/subtract", response_model=CalculationResponse)
def subtract(request: CalculationRequest):
    result = perform_calculation(request.operand1, request.operand2, "subtract")
    history.append((request.operand1, request.operand2, "subtract", result))
    return CalculationResponse(num1=request.operand1, num2=request.operand2, operation="subtract", result=result)

@app.post("/multiply", response_model=CalculationResponse)
def multiply(request: CalculationRequest):
    result = perform_calculation(request.operand1, request.operand2, "multiply")
    history.append((request.operand1, request.operand2, "multiply", result))
    return CalculationResponse(num1=request.operand1, num2=request.operand2, operation="multiply", result=result)

@app.post("/divide", response_model=CalculationResponse)
def divide(request: CalculationRequest):
    result = perform_calculation(request.operand1, request.operand2, "divide")
    history.append((request.operand1, request.operand2, "divide", result))
    return CalculationResponse(num1=request.operand1, num2=request.operand2, operation="divide", result=result)

@app.get("/history", response_model=list[CalculationResponse])
def get_history():
    return [CalculationResponse(num1=n1, num2=n2, operation=op, result=r) for n1, n2, op, r in history]
