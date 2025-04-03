from fastapi import APIRouter

from f_admin_client.routers import router as admin_router

router = APIRouter(prefix='/api', tags=['api'])
router.include_router(admin_router)


__all__ = ('router',)
