import sys
import www.orm
import asyncio,logging
from www.models import User, Blog, Comment

async def test(loop):
    await www.orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u=User(name='test22',email='test22@test.com',passwd='test',image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)