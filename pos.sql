CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    product_category TEXT NOT NULL,
    product_description TEXT,
    product_price REAL NOT NULL,
    product_quantity INTEGER NOT NULL
);

INSERT INTO Products (product_name, product_category, product_description, product_price, product_quantity)
VALUES ('Dog Food', 'Pet Food', 'Premium dog food', 20.99, 100),
       ('Cat Food', 'Pet Food', 'Healthy cat food', 15.99, 150),
       ('Fish Tank', 'Aquariums', '20-gallon glass fish tank', 100.00, 50),
       ('Dog Leash', 'Pet Supplies', 'Leather dog leash', 19.99, 75),
       ('Cat Litter', 'Pet Supplies', 'Odor-neutralizing cat litter', 9.99, 200);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT NOT NULL,
    total_price REAL NOT NULL
);

INSERT INTO Orders (order_date, total_price)
VALUES ('2022-02-15', 100.00),
       ('2022-02-16', 60.98),
       ('2022-02-16', 35.97);

CREATE TABLE Order_Details (
    order_detail_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders (order_id),
    FOREIGN KEY (product_id) REFERENCES Products (product_id)
);

INSERT INTO Order_Details (order_id, product_id, quantity, price)
VALUES (1, 1, 2, 41.98),
       (1, 3, 1, 100.00),
       (2, 2, 3, 47.97),
       (3, 5, 2, 19.98),
       (3, 4, 1, 19.99);
