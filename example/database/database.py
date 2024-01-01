from clio import SQLAlchemy

from example.config.config import get_database_path

db_file = get_database_path()
db_path = db_file.resolve()
sqlite_uri = f"sqlite:///{db_path}"

db = SQLAlchemy(sqlite_uri or "", echo=False)
