CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position VARCHAR(50) DEFAULT '',
    login VARCHAR(50) DEFAULT '',
    password VARCHAR(50) DEFAULT '',
    power_level INTEGER DEFAULT 0
);

CREATE TABLE Plays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) DEFAULT '',
    author VARCHAR(50) DEFAULT '',
    description VARCHAR(50) DEFAULT ''
);

CREATE TABLE Applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DateField(null=True),
    play_id INTEGER DEFAULT 0,
    count_tickets INTEGER DEFAULT 0,
    FOREIGN KEY (play_id) REFERENCES Plays(id)
);

CREATE TABLE Performances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) DEFAULT '',
    date DateField(null=True),
    play_id INTEGER DEFAULT 0,
    price INTEGER DEFAULT 0,
    FOREIGN KEY (play_id) REFERENCES Plays(id)
);

CREATE TABLE Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    performance_id INTEGER DEFAULT 0,
    fio VARCHAR(50) DEFAULT '',
    email VARCHAR(50) DEFAULT '',
    Comments VARCHAR(50) DEFAULT '',
    FOREIGN KEY (performance_id) REFERENCES Performances(id)
);

CREATE TABLE Seats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_num INTEGER DEFAULT 0,
    order_num INTEGER DEFAULT 0
);

CREATE TABLE Sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Application_number INTEGER DEFAULT 0,
    Place_number INTEGER DEFAULT 0,
    Buyer_id INTEGER DEFAULT 0,
    The_amount TEXT DEFAULT '',
    FOREIGN KEY (Application_number) REFERENCES Applications(id),
    FOREIGN KEY (Place_number) REFERENCES Seats(id),
    FOREIGN KEY (Buyer_id) REFERENCES Customers(id)
);
