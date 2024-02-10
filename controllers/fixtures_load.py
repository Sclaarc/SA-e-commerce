#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import *
import datetime
from decimal import *
from connexion_db import get_db
import time;
fixtures_load = Blueprint('fixtures_load', __name__,
                        template_folder='templates')

@fixtures_load.route('/base/init')
def fct_fixtures_load():
    mycursor = get_db().cursor()
    sql = '''DROP TABLE IF EXISTS `Ligne_panier`;
    '''
    mycursor.execute(sql)

    sql = '''DROP TABLE IF EXISTS `Ligne_commande`;
         '''
    mycursor.execute(sql)

    sql = '''DROP TABLE IF EXISTS `Declinaison`;
     '''
    mycursor.execute(sql)

    sql = '''DROP TABLE IF EXISTS `Commande`;
     '''
    mycursor.execute(sql)

    sql = '''DROP TABLE IF EXISTS `Avis`;
     '''
    mycursor.execute(sql)
    sql = '''DROP TABLE IF EXISTS `Adresse`;
     '''
    mycursor.execute(sql)
    sql = '''DROP TABLE IF EXISTS `Chaussure`;
     '''
    mycursor.execute(sql)
    sql = '''DROP TABLE IF EXISTS `Utilisateur`;
     '''
    mycursor.execute(sql)

    sql = '''DROP TABLE IF EXISTS `Etat`;
     '''
    mycursor.execute(sql)
    sql = '''DROP TABLE IF EXISTS `Pointure`;
     '''
    mycursor.execute(sql)
    sql = '''DROP TABLE IF EXISTS `Type_Chaussure`;
     '''
    mycursor.execute(sql)


    sql = ''' 

CREATE TABLE IF NOT EXISTS `Adresse` (
  `id_adresse` int NOT NULL AUTO_INCREMENT,
  `nom_complet` varchar(255) DEFAULT NULL,
  `rue` varchar(255) DEFAULT NULL,
  `code_postal` int DEFAULT NULL,
  `ville` varchar(255) DEFAULT NULL,
  `id_utilisateur` int NOT NULL,
  PRIMARY KEY (`id_adresse`),
  KEY `id_utilisateur` (`id_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
'''

    mycursor.execute(sql)









    sql = '''CREATE TABLE IF NOT EXISTS `Avis` (
  `id_avis` int NOT NULL AUTO_INCREMENT,
  `id_utilisateur` int DEFAULT NULL,
  `id_chaussure` int DEFAULT NULL,
  `libelle` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id_avis`),
  KEY `id_utilisateur` (`id_utilisateur`),
  KEY `id_chaussure` (`id_chaussure`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''



    mycursor.execute(sql)


    sql = '''CREATE TABLE IF NOT EXISTS `Chaussure` (
  `id_chaussure` int NOT NULL AUTO_INCREMENT,
  `nom_chaussure` varchar(50) NOT NULL,
  `sexe` varchar(20) NOT NULL,
  `prix_de_chaussure` decimal(15,2) DEFAULT NULL,
  `fournisseur` varchar(50) DEFAULT NULL,
  `marque` varchar(50) DEFAULT NULL,
  `entretien` varchar(50) DEFAULT NULL,
  `id_type_chaussure` int NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `commentaire` varchar(255) DEFAULT NULL,
  `image` varchar(255) NOT NULL,
  PRIMARY KEY (`id_chaussure`),
  KEY `id_type_chaussure` (`id_type_chaussure`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
'''

    mycursor.execute(sql)

    sql = '''
INSERT INTO `Chaussure` (`id_chaussure`, `nom_chaussure`, `sexe`, `prix_de_chaussure`, `fournisseur`, `marque`, `entretien`, `id_type_chaussure`, `description`, `commentaire`, `image`) VALUES
(1, 'Tennis Old Skool', 'M', '80.00', 'Espagne', 'Vans', 'Tissu', 1, 1,  NULL, '(1.1)baskets-vans-Tennis_Old_Skool.jpg'),
(2, 'Harlow', 'H', '80.00', 'Italie', 'Tommy Hilfiger', 'Tissu', 1, 1,  NULL, '(1.1)baskets-tommy_hilfiger-harlow.jpg'),
(3, 'Seneca Bay Slip On', 'H', '102.00', 'Espagne', 'Timberland', 'Tissu', 1, 1,  NULL, '(1.1)basket-timberland-seneca_bay_slip_on.jpg'),
(4, 'Chuck Taylor All Star', 'H', '83.00', 'France', 'Converse', 'Tissu', 1, 1,  NULL, '(1.1)baskets-converse-chuck_taylor_all_star.jpg'),
(5, 'Espadrille Cv Ns', 'M', '89.00', 'France', 'Calvin Klein', 'Tissu', 1, 6,  NULL, '(1.1)espadrilles-calvin_klein-Espadrille_Cv_Ns.jpg'),
(6, 'Uhabia 123 1 Cma', 'M', '130.00', 'Angleterre', 'Lacoste', 'Tissu', 1, 6,  NULL, '(1.1)espadrilles-lacoste-Uhabia_123_1_Cma.jpg'),
(7, 'Mini Bailey Bow', 'F', '219.95', 'Angleterre', 'UGG', 'Tissu', 1, 2,  NULL, '(1.1)bottes_ugg-Mini Bailey Bow.jpg'),
(8, 'Tongs E200104 Black 001', 'M', '666.00', 'Italie', 'Giuseppe Zanotti', 'Synthétique haute qualité', 1, 7,  NULL, '(1.1)tongs-Giuseppe_Zanotti-Tongs_E200104_Black_001.jpg'),
(9, 'Tongs Lemonbeach 24598703 Black G00', 'M', '43.00', 'France', 'Gant', 'Synthétique haute qualité', 1, 7,  NULL, '(1.1)tongs-Gant-Tongs_Lemonbeach_24598703_Black_G00.jpg'),
(10, 'Rigel Mid Wmn Trekking Shoes', 'F', '83.00', 'Italie', 'CMP', 'Tissu', 1, 3,  NULL, '(1.1)trekking-CMP-Rigel_Mid_Wmn_Trekking_Shoes.jpg'),
(11, 'Air Jordan 5 retro', 'M', '221.00', 'Angleterre', 'Nike', 'Tissu', 1, 1,  NULL, '(1.1)baskets-nike-air-jordan-5-face3-retro-low-.jpg'),
(12, 'WS14438-02', 'F', '30.99', 'France', 'Jenny Fairy', 'Tissu', 1, 2,  NULL, '(1.1)bottes-JennyFairy-WS14438-02.jpg'),
(13, 'MOSE-20 MBS', 'H', '27.99', 'Espagne', 'Lanetti', 'Cuir', 1, 4,  NULL, '(1.1)chaussures_basses-lanetti-MOSE_20 MBS.jpg'),
(14, 'GCD001F1TMELYBGP', 'M', '21.99', 'Espagne', 'Gap', 'Tissu', 1, 8,  NULL, '(1.1)mules-gap-GCD001F1TMELYBGP.jpg'),
(15, 'Air force 1', 'M', '149.99', 'Angleterre', 'Nike', 'Cuir', 1, 1,  NULL, '(1.1)baskets-nike-air_force_one.jpg'),
(16, 'Air Max Plus DZ4507 600 University', 'M', '199.99', 'Italie', 'Nike', 'Tissu', 1, 1,  NULL, '(1.1)baskets-nike-Air_Max_Pluas_DZ4507_600_University.jpg'),
(17, 'JA10089G1IIM0715', 'F', '187.00', 'Italie', 'Love Moschinos', 'Cuir', 1, 5,  NULL, '(1.1)talons_aiguilles-love_moschinos-JA10089G1IIM0715.jpg'),
(18, 'Felicity D36G1A 04340 C0013', 'F', '99.99', 'France', 'Geox', 'Cuir', 1, 2,  NULL, '(1.1)botte-geox-Felicity_D36G1A_04340_C0013.jpg'),
(19, 'ROSE-V1520-15', 'F', '90.99', 'France', 'Eva Minge', 'Cuir', 1, 5,  NULL, '(1.1)talons_aiguilles-eva_minge-ROSE_V1520_15.jpg'),
(20, 'Loeafers Espadrilles K 1.5 Patriot', 'H', '89.99', 'Italie', 'Manebi', 'Tissu', 1, 6,  NULL, '(1.1)espadrilles-manebi-Loeafers_Espadrilles_K_1.5_Patriot.jpg');
'''
    mycursor.execute(sql)

    sql = ''' 
CREATE TABLE IF NOT EXISTS `Commande` (
  `id_commande` int NOT NULL AUTO_INCREMENT,
  `date_achat` date NOT NULL,
  `id_utilisateur` int NOT NULL,
  `id_etat` int DEFAULT NULL,
  PRIMARY KEY (`id_commande`),
  KEY `id_utilisateur` (`id_utilisateur`),
  KEY `id_etat` (`id_etat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
'''
    mycursor.execute(sql)

    sql = ''' 

CREATE TABLE IF NOT EXISTS `Declinaison` (
  `Id_declinaison` int NOT NULL AUTO_INCREMENT,
  `id_pointure` int NOT NULL,
  `id_chaussure` int NOT NULL,
  `stock` int NOT NULL DEFAULT 10, 
  PRIMARY KEY (`Id_declinaison`),
  KEY `id_pointure` (`id_pointure`),
  KEY `id_chaussure` (`id_chaussure`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''
    mycursor.execute(sql)



    sql='''
CREATE TABLE IF NOT EXISTS `Etat` (
  `id_etat` int NOT NULL AUTO_INCREMENT,
  `libelle_etat` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_etat`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 ;'''
    mycursor.execute(sql)


    sql='''INSERT INTO `Etat` (`id_etat`, `libelle_etat`) VALUES
(1, 'En attente de traitement'),
(2, 'En cours de traitement'),
(3, 'Expédiée'),
(4, 'En transit'),
(5, 'Arrivée à destination'),
(6, 'Livraison en cours'),
(7, 'Livré'),
(8, 'Annulé'),
(9, 'Retourné');  '''
    mycursor.execute(sql)



    sql='''CREATE TABLE IF NOT EXISTS `Ligne_commande` (
  `Id_ligne_commande` int NOT NULL AUTO_INCREMENT,
  `quantité` int NOT NULL,
  `prix` decimal(7,2) NOT NULL,
  `Id_declinaison` int NOT NULL,
  `id_commande` int NOT NULL,
  `id_chaussure` int NOT NULL,
  PRIMARY KEY (`Id_ligne_commande`),
  KEY `Id_declinaison` (`Id_declinaison`),
  KEY `id_commande` (`id_commande`),
  KEY `id_chaussure` (`id_chaussure`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
'''
    mycursor.execute(sql)
#    sql = '''
#    INSERT INTO etat (libelle_etat) VALUES
#('En attente de traitement'),
#('En cours de traitement'),
#('Expédiée'),
#('En transit'),
#('Arrivée à destination'),
#('Livraison en cours'),
#('Livré'),
#('Annulé'),
#('Retourné');
#
#     '''
#    mycursor.execute(sql)

    sql = ''' 
CREATE TABLE IF NOT EXISTS `Ligne_panier` (
  `id_ligne` int NOT NULL AUTO_INCREMENT,
  `quantite` int DEFAULT NULL,
  `date_ajout` date DEFAULT NULL,
  `Id_declinaison` int NOT NULL,
  `id_utilisateur` int NOT NULL,
  PRIMARY KEY (`id_ligne`),
  KEY `Id_declinaison` (`Id_declinaison`),
  KEY `id_utilisateur` (`id_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
     '''
    mycursor.execute(sql)


    sql = ''' CREATE TABLE IF NOT EXISTS `Pointure` (
  `id_pointure` int NOT NULL,
  `libelle_pointure` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_pointure`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;'''
    mycursor.execute(sql)

    sql = '''INSERT INTO `Pointure` (`id_pointure`, `libelle_pointure`) VALUES
(1, '35'),
(2, '36'),
(3, '37'),
(4, '38'),
(5, '39'),
(6, '40'),
(7, '41'),
(8, '42'),
(9, '43'),
(10, '44'),
(11, '45'),
(12, '46'),
(13, '47'),
(14, '48');'''
    mycursor.execute(sql)

    sql = '''
CREATE TABLE IF NOT EXISTS `Type_Chaussure` (
  `id_type_chaussure` int NOT NULL AUTO_INCREMENT,
  `libelle_type_chaussure` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_type_chaussure`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 ;
 '''

    mycursor.execute(sql)

    sql = '''
CREATE TABLE IF NOT EXISTS `Utilisateur` (
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  `login` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 ;'''

    mycursor.execute(sql)


    sql = '''INSERT INTO `Utilisateur` (`id_utilisateur`, `login`, `email`, `nom`, `password`, `role`) VALUES
(1, 'admin', 'admin@admin.fr', 'admin', 'pbkdf2:sha256:600000$NjWXimmhMhSJXMGn$b61103d8cc109da068ce84239b41889df5baac6081f6aeecfe840b68883fdc91', 'ROLE_admin'),
(2, 'client', 'client@client.fr', 'client', 'pbkdf2:sha256:600000$VrqIAlFLfqJpqe3p$b6f342deaaef485293d978654586fec822ed3d0f339a14f9af749e165262f8b4', 'ROLE_client'),
(3, 'client2', 'client2@client2.fr', 'client2', 'pbkdf2:sha256:600000$J4DcklkBGeVc5Tap$d59f8a8deed4918e1ae7f704783c4274b82a6122949816f001cd1157d9ad4e2b', 'ROLE_client');
'''
    mycursor.execute(sql)

    sql = '''INSERT INTO `Type_Chaussure` (`id_type_chaussure`, `libelle_type_chaussure`) VALUES
(1, 'Baskets'),
(2, 'Espadrilles'),
(3, 'Sandales'),
(4, 'Bottes'),
(5, 'Talons'),
(6, 'Baskets'),
(7, 'Bottes'),
(8, 'Trekking'),
(9, 'Chaussures basses'),
(10, 'Talons aiguilles'),
(11, 'Espadrilles'),
(12, 'Tongs'),
(13, 'Mules');
'''

    mycursor.execute(sql)

    sql = '''INSERT INTO Declinaison (id_pointure,id_chaussure) VALUES
(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(14,1),

(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),(12,2),(13,2),(14,2),

(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(14,3),

(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(12,4),(13,4),(14,4),

(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),(12,5),(13,5),(14,5),

(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(10,6),(11,6),(12,6),(13,6),(14,6),

(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),(12,7),(13,7),(14,7);


'''

    mycursor.execute(sql)

    sql = ''' INSERT INTO `Utilisateur` (`id_utilisateur`, `login`, `email`, `nom`, `password`, `role`) VALUES
(4, 'mdagbert', 'matou68200@gmail.com', 'cmoiwesh', 'pbkdf2:sha256:600000$DZqqK1LVN4pIA0KF$5c7c94e493243de9e31fd185d362a00c9a47cf95cb151355ecdc5db1c4de690f', 'ROLE_admin'),
(5, 'test', 'testmail@gamil.com', 'catest', 'pbkdf2:sha256:600000$NnSXxO1w5LfDtWdw$edfebfeefcb146eb54556fc1405f07066f9de58a87b6cb6faa784c64f3363a99', 'ROLE_client');


'''
    mycursor.execute(sql)

    sql = '''
    ALTER TABLE `Adresse`
  ADD CONSTRAINT `Adresse_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `Utilisateur` (`id_utilisateur`);

    '''
    mycursor.execute(sql)

    sql = '''
    ALTER TABLE `Avis`
  ADD CONSTRAINT `Avis_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `Utilisateur` (`id_utilisateur`),
  ADD CONSTRAINT `Avis_ibfk_2` FOREIGN KEY (`id_chaussure`) REFERENCES `Chaussure` (`id_chaussure`);

    '''
    mycursor.execute(sql)



    sql = '''
    ALTER TABLE `Commande`
  ADD CONSTRAINT `Commande_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `Utilisateur` (`id_utilisateur`),
  ADD CONSTRAINT `Commande_ibfk_2` FOREIGN KEY (`id_etat`) REFERENCES `Etat` (`id_etat`);

    '''
    mycursor.execute(sql)

    sql = '''
    ALTER TABLE `Declinaison`
  ADD CONSTRAINT `Declinaison_ibfk_1` FOREIGN KEY (`id_pointure`) REFERENCES `Pointure` (`id_pointure`),
  ADD CONSTRAINT `Declinaison_ibfk_2` FOREIGN KEY (`id_chaussure`) REFERENCES `Chaussure` (`id_chaussure`);

    '''
    mycursor.execute(sql)

    sql = '''
    ALTER TABLE `Ligne_commande`
  ADD CONSTRAINT `Ligne_commande_ibfk_1` FOREIGN KEY (`Id_declinaison`) REFERENCES `Declinaison` (`Id_declinaison`),
  ADD CONSTRAINT `Ligne_commande_ibfk_2` FOREIGN KEY (`id_commande`) REFERENCES `Commande` (`id_commande`),
  ADD CONSTRAINT `Ligne_commande_ibfk_3` FOREIGN KEY (`id_chaussure`) REFERENCES `Chaussure` (`id_chaussure`);

    '''
    mycursor.execute(sql)

    sql = '''
    ALTER TABLE `Ligne_panier`
  ADD CONSTRAINT `Ligne_panier_ibfk_1` FOREIGN KEY (`Id_declinaison`) REFERENCES `Declinaison` (`Id_declinaison`),
  ADD CONSTRAINT `Ligne_panier_ibfk_2` FOREIGN KEY (`id_utilisateur`) REFERENCES `Utilisateur` (`id_utilisateur`);

    '''
    mycursor.execute(sql)


    get_db().commit()


    return redirect('/')

