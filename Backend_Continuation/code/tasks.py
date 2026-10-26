import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_book_created(book_id: int, title: str) -> None:
    logger.info(
        "Background task: book created | id=%s | title=%s",
        book_id,
        title,
    )