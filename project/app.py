import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from apps.routers import router as api_router
from conf import settings

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS
)
app.include_router(router=api_router)

# Вынесем сюда, ибо не пересчитывается после считывания env файла
TORTOISE_CONFIG = {
    'generate_schemas': True,
    'add_exception_handlers': True,
    'timezone': settings.TIMEZONE,
    'connections': {'default': settings.DATABASE_URL},
    'apps': {
        'models': {
            'models': settings.APP_MODELS,
            'default_connection': 'default',
        },
    },
}

register_tortoise(app, config=TORTOISE_CONFIG)


if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)
