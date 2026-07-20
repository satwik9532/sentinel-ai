from contextlib import contextmanager

from sqlalchemy.orm import Session


@contextmanager
def transaction(db: Session):
    """
    Transaction context manager.
    """

    try:
        yield

        db.commit()

    except Exception:
        db.rollback()

        raise
