from sqlalchemy import Column, Integer, inspect, LargeBinary, Text

from database import Base, engine


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    project_name = Column(Text)
    introduction = Column(Text)
    description = Column(Text)
    image = Column(LargeBinary)

    @classmethod
    def create_if_not_table(cls):
        if not inspect(engine).has_table(cls.__tablename__):
            Base.metadata.create_all(bind=engine)

