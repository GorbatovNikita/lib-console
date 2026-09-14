from functools import wraps
from database.session import SessionLocal

def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with SessionLocal() as session:
            try:
                result = func(session, *args, **kwargs)
                session.commit()
                return result
            except Exception:
                session.rollback()
                raise
    return wrapper