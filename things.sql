DROP TABLE things;

CREATE TABLE things (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name TEXT,
    description TEXT,
    location TEXT,
    status TEXT DEFAULT "on"
);

INSERT INTO things (name, description, location) VALUES
('Bagulho', 'Apenas um bagulho', 'Em uma caixa'),
('Tranqueira', 'Apenas uma tranqueira qualquer', 'Em um gaveteiro qualquer'),
('Bagulete', 'Apenas um bagulete qualquer', 'Em um caixote na esquina');
