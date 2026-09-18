import duckdb

# This creates (or opens) a database file called warehouse.duckdb
con = duckdb.connect("warehouse.duckdb")

con.execute("""
    CREATE SCHEMA IF NOT EXISTS raw;
""")

con.execute("""
    CREATE OR REPLACE TABLE raw.weather AS
    SELECT * FROM read_csv_auto('raw_weather.csv')
""")

print(con.execute("SELECT * FROM raw.weather LIMIT 5").fetchdf())
con.close()