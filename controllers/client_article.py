#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, abort, flash, session

from connexion_db import get_db

client_article = Blueprint('client_article', __name__,
                        template_folder='templates')

@client_article.route('/client/index')
@client_article.route('/client/article/show')              # remplace /client
def client_article_show():                                 # remplace client_index
    mycursor = get_db().cursor()
    id_client = session['id_user']

    list_param = []
    condition_and = ""
    # utilisation du filtre

    if "filtre_mot" in session or "filtre_min" in session or "filtre_max" in session or "filter_types" in session:
        sql = '''   SELECT 
            id_chaussure AS IdChaussure,
            nom_chaussure AS NomChaussure,
            entretien AS Entretien,
            sexe AS Sexe,
            prix_de_chaussure AS PrixChaussure,
            id_type_chaussure AS TypeChaussureId,
            fournisseur AS Fournisseur,
            marque AS Marque,
            image AS Image
        FROM Chaussure WHERE
           '''

    else:
        sql = '''    
    SELECT Chaussure.id_chaussure AS IdChaussure,
        Chaussure.nom_chaussure AS NomChaussure,
        Chaussure.entretien AS Entretien,
        Chaussure.sexe AS Sexe,
        Chaussure.prix_de_chaussure AS PrixChaussure,
        Chaussure.id_type_chaussure AS TypeChaussureId,
        Chaussure.fournisseur AS Fournisseur,
        Chaussure.marque AS Marque,
        Chaussure.image AS Image,
        d.Id_declinaison,
        p.libelle_pointure,
        d.stock AS Stock
FROM Declinaison d
JOIN Chaussure ON d.id_chaussure = Chaussure.id_chaussure
JOIN Pointure p ON d.id_pointure = p.id_pointure
where d.id_pointure = 1
ORDER BY Chaussure.id_chaussure, p.libelle_pointure
;'''
    if "filtre_mot" in session:
        sql = sql + " nom_chaussure like %s "
        recherche = "%" + session["filtre_mot"] + "%"
        list_param.append(recherche)
        condition_and = " AND "
    if "filtre_min" in session or "filtre_max" in session:
        sql = sql + condition_and + " prix_de_chaussure BETWEEN %s AND %s "
        list_param.append(session["filtre_min"])
        list_param.append(session["filtre_max"])
        condition_and = " AND "
    if "filter_types" in session:
        sql = '''   SELECT 
                    id_chaussure AS IdChaussure,
                    nom_chaussure AS NomChaussure,
                    entretien AS Entretien,
                    sexe AS Sexe,
                    prix_de_chaussure AS PrixChaussure,
                    id_type_chaussure AS TypeChaussureId,
                    fournisseur AS Fournisseur,
                    marque AS Marque,
                    image AS Image
                FROM Chaussure where
                   '''
        last_item = session['filter_types'][-1]
        for item in session['filter_types']:
            sql = sql + "id_type_chaussure = %s "
            if item != last_item:
                sql = sql + " or "
            list_param.append(item)


    tuple_sql = tuple(list_param)
    print(sql)
    mycursor.execute(sql, tuple_sql)
    Chaussure = mycursor.fetchall()

    #articles =[]
    sql = '''   SELECT 
    id_type_chaussure as IdTypeChaussure,
    libelle_type_chaussure as LibelleTypeChaussure
    FROM Type_Chaussure;
       '''
    list_param = []
    condition_and = ""
    # utilisation du filtre
    sql3 = ''' prise en compte des commentaires et des notes dans le SQL    '''
    mycursor.execute(sql)
    types_chaussure = mycursor.fetchall()
    sql='''    
    SELECT Ligne_panier.id_ligne as IdLigne
    , Ligne_panier.quantite as Quantite
    , Ligne_panier.date_ajout as DateAjout
    , Ligne_panier.id_utilisateur as UtilisateurId
    ,Ligne_panier.id_chaussure as ChaussureId
    ,Chaussure.nom_chaussure as ChaussureNom
    , Chaussure.prix_de_chaussure as ChaussurePrix,

FROM Ligne_panier
JOIN Chaussure ON Ligne_panier.id_chaussure = Chaussure.id_chaussure
where id_utilisateur=%s
;
'''
    #mycursor.execute(sql,(id_client,))
    Ligne_panier = mycursor.fetchall()
    # pour le filtre
    #types_article = []


    articles_panier = []

    if len(articles_panier) >= 1:
        sql = ''' calcul du prix total du panier '''
        prix_total = None
    else:
        prix_total = None
    return render_template('client/boutique/panier_article.html'
                           , Chaussure=Chaussure
                           , articles_panier=articles_panier
                           #, prix_total=prix_total
                           , Ligne_panier=Ligne_panier
                           , types_chaussure=types_chaussure
                           )
