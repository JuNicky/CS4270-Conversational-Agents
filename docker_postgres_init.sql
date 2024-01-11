DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS cocktail_data;

CREATE TABLE Users
(
    id serial PRIMARY KEY,
    name text NOT NULL,
    age integer,
    visit integer,
    last_drink text,
    preferred_sweet integer CHECK (preferred_sweet BETWEEN 1 AND 5),
    preferred_sour integer CHECK (preferred_sour BETWEEN 1 AND 5)
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

COPY cocktail_data(id, alcoholic, drink, glass, ingredients, ingredients_and_quantities, instructions)
FROM '/docker-entrypoint-initdb.d/data/cocktail_data_one.csv' DELIMITER ',' CSV HEADER;
