import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # ─── Security Keys ─────────────────────────────────────────────
    SECRET_KEY = os.getenv("SECRET_KEY", "smart-task-mvc-secret-2024")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-smart-task-mvc-2024")

    # ─── Railway MySQL Environment Variables ───────────────────────
    DB_USER = os.getenv("MYSQLUSER")
    DB_PASSWORD = os.getenv("MYSQLPASSWORD")
    DB_HOST = os.getenv("MYSQLHOST")
    DB_PORT = os.getenv("MYSQLPORT", "3306")
    DB_NAME = os.getenv("MYSQLDATABASE")

    # ─── SQLAlchemy Database URI ───────────────────────────────────
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ─── File Upload Settings ──────────────────────────────────────
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    ALLOWED_EXTENSIONS = {
        "png", "jpg", "jpeg", "gif",
        "pdf", "doc", "docx",
        "txt", "xlsx", "csv", "zip"
    }

    # ─── JWT Settings ──────────────────────────────────────────────
    JWT_ACCESS_TOKEN_EXPIRES = False