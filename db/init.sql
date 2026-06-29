CREATE DATABASE IF NOT EXISTS techsecure_db;
USE techsecure_db;

CREATE TABLE IF NOT EXISTS filiales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ville VARCHAR(100) NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    responsable VARCHAR(100) NOT NULL,
    employes INT NOT NULL,
    ip_reseau VARCHAR(50) NOT NULL
);

-- Insertion des données de base demandées par le TP
INSERT INTO filiales (ville, adresse, responsable, employes, ip_reseau) VALUES
('Paris', '12 Rue de la Paix, 75002 Paris', 'Jean Dupont', 45, '10.10.1.1'),
('Lyon', '45 Rue de la République, 69002 Lyon', 'Marie Curie', 28, '10.10.2.1'),
('Marseille', '88 Quai du Port, 13002 Marseille', 'Pierre Martin', 17, '10.10.3.1');