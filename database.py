
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# DATABASE_URL = "postgresql://root:root@localhost/logs"
USER_DB = "root"
PASSWORD_DB = "root"
NAME_DB = "logs"

DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@localhost/{NAME_DB}"

engine = _sql.create_engine(DATABASE_URL) 

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()