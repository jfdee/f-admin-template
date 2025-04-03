from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "register_at" DATE;
        ALTER TABLE "user" ADD "blocked_at" TIMESTAMPTZ;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "register_at";
        ALTER TABLE "user" DROP COLUMN "blocked_at";"""
