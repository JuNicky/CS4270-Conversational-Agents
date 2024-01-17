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
    sweet boolean,
    sour boolean,
    spicy boolean,
    -- bitter boolean, 
    fruity boolean,
    savory boolean,
    hot boolean,
    frozen boolean,
    refreshing boolean
);

CREATE TABLE cocktail_data (
    id serial PRIMARY KEY,
    alcoholic text,
    drink text,
    glass text,
    ingredients text,
    ingredients_and_quantities text,
    instructions text
);

COPY cocktail_data FROM '/docker-entrypoint-initdb.d/data/cocktail_data_one.csv' CSV HEADER;
