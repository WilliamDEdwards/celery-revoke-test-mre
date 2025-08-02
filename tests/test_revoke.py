from utils import revoke_test

def test_noop(celery_worker):
    pass

def test_revoke(celery_worker):
    revoke_test()