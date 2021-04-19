import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import settings
from app.migrations import migrate
from app.views import router


def init_app():
    app = FastAPI(
        title=settings.SERVICE_NAME,
        debug=settings.DEBUG_MODE,
        docs_url="/docs",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    return app


if __name__ == "__main__":
    print('Start migration...')
    try:
        migrate()
    except Exception as ex:
        print(ex)
    print('Done.')

    print('Start app...')
    uvicorn.run(
        init_app(),
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        workers=settings.APP_WORKER_COUNT,
        loop="uvloop",
        log_config=settings.LOG_CONFIG,
        log_level=logging.getLevelName(settings.LOG_LEVEL),
    )
