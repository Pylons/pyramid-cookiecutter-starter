from sqlalchemy import Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(Text)
    value: Mapped[Optional[int]] = mapped_column(Integer)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
