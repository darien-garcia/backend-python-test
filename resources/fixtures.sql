INSERT INTO users (username, password) VALUES
('user1', 'pbkdf2:sha256:150000$yeGvn7d5$d50dd5f9ee537282c6c4fd6efdbd30bc37fa6de78e4589b74eefb99b2c570a77'),
('user2', 'pbkdf2:sha256:150000$28Qvc7m3$8b0dda05107d3aad28419f9efc3ed44223734208a77ca8e3c7e02efe99b34572'),
('user3', 'pbkdf2:sha256:150000$Bt8sAi5l$a4387e292debef820d97fa43517c13e5b8c7120a7a788f74e8bb40e9c7d1c59f');

INSERT INTO todos (user_id, description) VALUES
(1, 'Vivamus tempus'),
(1, 'lorem ac odio'),
(1, 'Ut congue odio'),
(1, 'Sodales finibus'),
(1, 'Accumsan nunc vitae'),
(2, 'Lorem ipsum'),
(2, 'In lacinia est'),
(2, 'Odio varius gravida');