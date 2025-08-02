from utils import revoke_test

def test_noop():
    pass

def test_revoke(celery_worker):
    revoke_test()