psql
CREATE DATABASE geekbrains;
\c geekbrains

CREATE TABLE phones (
    id bigserial primary key,
    product_name varchar(33) NOT NULL,
    manufacturer varchar(33) NOT NULL,
    product_count integer NOT NULL,
    price integer NOT NULL
);

INSERT INTO phones (product_name, manufacturer, product_count, price)
VALUES ('Galaxy S9', 'Samsung', 4, 63000),
       ('iPhone X', 'Apple', 3, 71000),
       ('iPhone 6', 'Apple', 3, 36000),
       ('Galaxy S8', 'Samsung', 2, 46000),
       ('Galaxy S8 Plus', 'Samsung', 1, 56000),
       ('N6', 'Nokia', 5, 11000);

SELECT * FROM phones;

     id |  product_name  | manufacturer | product_count | price 
    ----+----------------+--------------+---------------+-------
      1 | Galaxy S9      | Samsung      |             4 | 63000
      2 | iPhone X       | Apple        |             3 | 71000
      3 | iPhone 6       | Apple        |             3 | 36000
      4 | Galaxy S8      | Samsung      |             2 | 46000
      5 | Galaxy S8 Plus | Samsung      |             1 | 56000
      6 | N6             | Nokia        |             1 | 11000
    (6 rows)

SELECT product_name, manufacturer, price FROM phones WHERE product_count > 2;

     product_name | manufacturer | price 
    --------------+--------------+-------
     Galaxy S9    | Samsung      | 63000
     iPhone X     | Apple        | 71000
     iPhone 6     | Apple        | 36000
    (3 rows)

SELECT * FROM phones WHERE manufacturer = 'Samsung';

     id |  product_name  | manufacturer | product_count | price 
    ----+----------------+--------------+---------------+-------
      1 | Galaxy S9      | Samsung      |             4 | 63000
      4 | Galaxy S8      | Samsung      |             2 | 46000
      5 | Galaxy S8 Plus | Samsung      |             1 | 56000
    (3 rows)

SELECT * FROM phones WHERE product_name iLIKE '%iphone%';

     id | product_name | manufacturer | product_count | price 
    ----+--------------+--------------+---------------+-------
      2 | iPhone X     | Apple        |             3 | 71000
      3 | iPhone 6     | Apple        |             3 | 36000
    (2 rows)

SELECT * FROM phones WHERE manufacturer iLIKE '%samsung%';

     id |  product_name  | manufacturer | product_count | price 
    ----+----------------+--------------+---------------+-------
      1 | Galaxy S9      | Samsung      |             4 | 63000
      4 | Galaxy S8      | Samsung      |             2 | 46000
      5 | Galaxy S8 Plus | Samsung      |             1 | 56000
    (3 rows)

SELECT * FROM phones WHERE product_name ~ '\d';

     id |  product_name  | manufacturer | product_count | price 
    ----+----------------+--------------+---------------+-------
      1 | Galaxy S9      | Samsung      |             4 | 63000
      3 | iPhone 6       | Apple        |             3 | 36000
      4 | Galaxy S8      | Samsung      |             2 | 46000
      5 | Galaxy S8 Plus | Samsung      |             1 | 56000
      6 | N6             | Nokia        |             1 | 11000
    (5 rows)

SELECT * FROM phones WHERE product_name ~ '8';

     id |  product_name  | manufacturer | product_count | price 
    ----+----------------+--------------+---------------+-------
      4 | Galaxy S8      | Samsung      |             2 | 46000
      5 | Galaxy S8 Plus | Samsung      |             1 | 56000
