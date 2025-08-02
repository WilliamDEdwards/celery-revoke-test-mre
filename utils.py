from celery.result import AsyncResult

import celery_app
from celery_app import noop,app

def revoke_test():
    print(app.control.inspect().scheduled())
    print(app.control.inspect().reserved())
    print(app.control.inspect().active())

    async_result = noop.apply_async(countdown=2)

    assert async_result.status == 'PENDING'

    print(app.control.revoke(async_result.id))

    import time; time.sleep(3)

    async_result = AsyncResult(async_result.id)

    assert async_result.status == 'REVOKED', async_result.status
