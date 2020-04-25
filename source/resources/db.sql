DROP TABLE IF EXISTS urls;
DROP TABLE IF EXISTS tme;
DROP TABLE IF EXISTS words;

create table tme(
                    id SERIAL PRIMARY KEY,
                    tme text,
                    url_name text UNIQUE
);

create table words(
                      id SERIAL PRIMARY KEY,
                      word text,
                      category text
);

create table urls(
                     id SERIAL PRIMARY KEY,
                     url text,
                     name text UNIQUE ,
                     category text
);

create table default_url(
                     url text,
                     name text,
                     category text
);
