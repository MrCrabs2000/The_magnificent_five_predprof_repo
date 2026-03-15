from flask_security import current_user
from flask import render_template, redirect
from pathlib import Path

from routes.routes import register_all_blueprints
from configs.configs import app
from utils.migrate import drop_alembic_version_table, update_database


register_all_blueprints(app)


try:
    db_path = Path(__file__).parent / 'db' / 'database.db'
    if not db_path.exists():
        drop_alembic_version_table(app)

    update_database(app)

except Exception as e:
    print(f'У нас ошибка в функции поймана:{e}')


@app.route('/')
def main():
    if current_user.is_authenticated:
        return render_template('main.html')
    return redirect('/login')


if '__main__' == __name__:
    app.run(debug=True)