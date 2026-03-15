from flask_security import current_user
from flask import redirect
from pathlib import Path

from routes.routes import register_all_blueprints
from configs.configs import app
from utils.migrate import drop_alembic_version_table, update_database
from configs.init_db import create_initial_admin


register_all_blueprints(app)


try:
    db_path = Path(__file__).parent / 'db' / 'database.db'
    if not db_path.exists():
        drop_alembic_version_table(app)

    update_database(app)
    create_initial_admin(app)

except Exception as e:
    print(f'У нас ошибка в функции поймана:{e}')


@app.route('/', methods=['GET', 'POST'])
def inition():
    if current_user.is_authenticated:
        if current_user.roles[0].name == 'user':
            return redirect('/user/main')
        elif current_user.roles[0].name == 'admin':
            return redirect('/admin/main')

    return redirect('/login')


if '__main__' == __name__:
    app.run(debug=True)