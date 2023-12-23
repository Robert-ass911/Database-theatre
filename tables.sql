CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position TEXT DEFAULT '',
    login TEXT DEFAULT '',
    password TEXT DEFAULT '',
    power_level INTEGER DEFAULT 0
);

CREATE TABLE Plays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT DEFAULT '',
    price TEXT DEFAULT '',
    description TEXT DEFAULT ''
);

CREATE TABLE Applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT DEFAULT '',
    play_id INTEGER DEFAULT 0,
    count_tickets INTEGER DEFAULT 0,
    FOREIGN KEY (play_id) REFERENCES Plays(id)
);

CREATE TABLE Performances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT DEFAULT '',
    date TEXT DEFAULT '',
    play_id INTEGER DEFAULT 0,
    price INTEGER DEFAULT 0,
    FOREIGN KEY (play_id) REFERENCES Plays(id)
);

CREATE TABLE Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    performance_id INTEGER DEFAULT 0,
    fio TEXT DEFAULT '',
    email TEXT DEFAULT '',
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