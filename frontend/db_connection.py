import sys
from pathlib import Path
from sqlalchemy import text

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from api.database import get_session

def get_cities():
    """
    Retorna lista de cidades distintas da tabela 'houses', ordenadas alfabeticamente.
    Remove valores None automaticamente.
    """
    session = next(get_session())
    try:
        result = session.execute(text("SELECT DISTINCT city FROM houses ORDER BY city;"))
        return [row[0] for row in result.fetchall() if row[0] is not None]
    finally:
        session.close()