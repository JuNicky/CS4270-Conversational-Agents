DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS cocktail_data;

CREATE TABLE Users
(
    id serial PRIMARY KEY,
    name text NOT NULL,
    age integer,
    visit integer,
    last_drink text,
    occasion text,
    sour boolean,
    cream boolean,
    bitter boolean,
    -- bitter boolean, 
    water boolean,
    herbal boolean,
    egg boolean,
    salty boolean,
    spicy boolean
);

CREATE TABLE cocktail_data (
    id serial PRIMARY KEY,
    alcoholic text,
    drink text,
    glass text,
    ingredients text,
    ingredients_and_quantities text,
    instructions text,
    sour boolean,
    sweet boolean,
    cream boolean,
    bitter boolean,
    water boolean,
    herbal boolean,
    egg boolean,
    salty boolean,
    spicy boolean
);

COPY cocktail_data FROM '/docker-entrypoint-initdb.d/data/updated_cocktail_data.csv' CSV HEADER;
