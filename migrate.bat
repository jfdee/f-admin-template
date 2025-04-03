@echo off

CD project

if not exist pyproject.toml (
    echo "init config..."
    aerich init -t app.TORTOISE_CONFIG
)

aerich init-db
aerich migrate
aerich upgrade
