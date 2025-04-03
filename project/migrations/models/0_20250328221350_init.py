from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "organization" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "full_name" VARCHAR(256) NOT NULL,
    "short_name" VARCHAR(256) NOT NULL,
    "address" VARCHAR(128) NOT NULL,
    "email" VARCHAR(128) NOT NULL
);
COMMENT ON COLUMN "organization"."created_at" IS 'Дата создания';
COMMENT ON COLUMN "organization"."full_name" IS 'Полное наименование';
COMMENT ON COLUMN "organization"."short_name" IS 'Краткое наименование';
COMMENT ON COLUMN "organization"."address" IS 'Адрес';
COMMENT ON COLUMN "organization"."email" IS 'Почта';
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "username" VARCHAR(128) NOT NULL,
    "email" VARCHAR(128) NOT NULL,
    "last_name" VARCHAR(256) NOT NULL,
    "first_name" VARCHAR(256) NOT NULL,
    "patronymic" VARCHAR(256),
    "is_blocked" BOOL NOT NULL  DEFAULT False,
    "organization_id" INT REFERENCES "organization" ("id") ON DELETE SET NULL
);
COMMENT ON COLUMN "user"."created_at" IS 'Дата создания';
COMMENT ON COLUMN "user"."username" IS 'Логин';
COMMENT ON COLUMN "user"."email" IS 'Почта';
COMMENT ON COLUMN "user"."last_name" IS 'Фамилия';
COMMENT ON COLUMN "user"."first_name" IS 'Имя';
COMMENT ON COLUMN "user"."patronymic" IS 'Отчество';
COMMENT ON COLUMN "user"."is_blocked" IS 'Заблокирован';
COMMENT ON COLUMN "user"."organization_id" IS 'Организация';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
