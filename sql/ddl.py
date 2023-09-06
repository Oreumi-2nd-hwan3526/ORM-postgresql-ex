import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "restaurant",
    user = "postgres",
    password = "1234",
    )

cursor = conn.cursor()

create_table_query = """
    -- Table: public.fastfood

    -- DROP TABLE IF EXISTS public.fastfood;

    CREATE TABLE IF NOT EXISTS public.fastfood
    (
        id character varying(30) COLLATE pg_catalog."default",
        "dateAdded" timestamp without time zone,
        "dateUpdated" timestamp without time zone,
        address character varying(100) COLLATE pg_catalog."default",
        categories character varying(100) COLLATE pg_catalog."default",
        city character varying(100) COLLATE pg_catalog."default",
        country character varying(30) COLLATE pg_catalog."default",
        keys character varying(200) COLLATE pg_catalog."default",
        latitude real,
        longitude real,
        name character varying(50) COLLATE pg_catalog."default",
        "postalCode" character varying(30) COLLATE pg_catalog."default",
        province character(2) COLLATE pg_catalog."default",
        "sourceURLs" text COLLATE pg_catalog."default",
        websites text COLLATE pg_catalog."default",
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.fastfood
        OWNER to postgres;
"""

cursor.execute(create_table_query)
conn.commit()
conn.close()