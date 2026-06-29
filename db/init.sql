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

-- Insertion des données initiales d'après le sujet
INSERT INTO filiales (ville, adresse, responsable, employes, ip_reseau) VALUES
('Paris', '12 Avenue de la Grande Armée, 75017 Paris', 'Jean Dupont', 85, '10.10.1.1'),
('Lyon', '42 Rue de la République, 69002 Lyon', 'Sophie Martin', 40, '10.10.2.1'),
('Marseille', '5 Place de la Joliette, 13002 Marseille', 'Marc Durand', 30, '10.10.3.1');