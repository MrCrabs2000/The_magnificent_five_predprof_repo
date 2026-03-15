from pathlib import Path
from flask_migrate import Migrate, upgrade, migrate
from database.classes import db
from sqlalchemy import text
import shutil


PRO_DIR = Path(__file__).parent.absolute()
MIGRATIONS_DIR = PRO_DIR / 'migrations'


def drop_alembic_version_table(app):
    with app.app_context():
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()

        if 'alembic_version' in tables:
            db.session.execute(text('DROP TABLE alembic_version'))
            db.session.commit()
            print("Таблица alembic_version успешно удалена")
        else:
            print("Таблица alembic_version не существует")

        if MIGRATIONS_DIR.exists() and MIGRATIONS_DIR.is_dir():
            shutil.rmtree(MIGRATIONS_DIR)
            print(f"Директория {MIGRATIONS_DIR} удалена")
        else:
            print(f"Директория {MIGRATIONS_DIR} не существует")


def update_database(app):
    migrateion = Migrate(app, db, directory=str(MIGRATIONS_DIR))

    with app.app_context():
        if not MIGRATIONS_DIR.exists():
            from flask_migrate import init as flask_init
            flask_init(directory=str(MIGRATIONS_DIR))

        try:
            migrate(message="automated migration", directory=str(MIGRATIONS_DIR))

            upgrade(directory=str(MIGRATIONS_DIR))
            
        except Exception as e:
            print(f'У нас ошибка в функции поймана: {e}')
            drop_alembic_version_table(app)


if __name__ == "__main__":
    from configs.configs import app
    update_database(app)