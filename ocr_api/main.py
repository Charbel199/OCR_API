import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.controllers import ocr_controller, health_check_controller

app = FastAPI(version='2.0', title='OCR Character Extractor',
              description="API for extracting characters from an image")

# app.mount("/models_services", StaticFiles(directory="/checkpoints/servable"), name="models_services")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )
app.include_router(
    ocr_controller.router,
    prefix="/extract",
    tags=["extract"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    health_check_controller.router,
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)
if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5555)
