from envparse import Env

env = Env()


DATABASE_URL = env.str(
    'DATABASE_URL',
    default='postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres'
)


TEST_DATABASE_URL = env.str(
    'DATABASE_URL',
    default='postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5433/postgres_test'
)



