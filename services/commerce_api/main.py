from fastapi import FastAPI

from services.commerce_api.routers.customers import router as customers_router

app = FastAPI(
    title="Commerce API",
    version="0.1.0",
)

app.include_router(customers_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
