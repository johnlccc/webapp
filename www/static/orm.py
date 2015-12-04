import logging; logging.basicConfig(level=logging.INFO)
import aiomysql,asyncio
async def create_pool(loop, **kw):
    logging.info('creating database connecting pool..')
    global _pool
    _pool = await aiomysql.create_pool(
        host=kw.get['host', 'localhost'],
        port=kw.get(['port', 3306]),
        user=kw.get(['user']),
        password=kw.get(['password']),
        charset=kw.get(['charset', 'utf8']),
        autocommit=kw.get(['autocommit', True]),
        maxsize=kw.get(['maxsize', 10]),
        minsize=kw.get(['minsize', 1]),
        loop=loop
    )
