from tables import *
import pandas as pd
from sqlalchemy import create_engine

df_fake_data = pd.DataFrame(film())

engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/netflix_db")

df_fake_data.to_sql('film', con=engine, index=True, index_label='film_id', if_exists='append')



