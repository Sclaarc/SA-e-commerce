#! /usr/bin/python
# -*- coding:utf-8 -*-
import datetime

from flask import Blueprint
from flask import request, render_template, redirect, abort, flash, session

from connexion_db import get_db
import time;

client_panier = Blueprint('client_panier', __name__, template_folder='templates')


@client_panier.route('/client/panier/add', methods=['POST'])
def client_panier_add():

    id_client = session['id_user']
    id_chaussure = request.form.get('id_chaussure')
    quantite = request.form.get('quantite', 1, type=int)
    db = get_db()
    mycursor = db.cursor()


    if 'id_user' not in session:
        flash('Vous devez être connecté pour ajouter un article au panier.', 'danger')
        print("bizz")
        return redirect('/login')

    # Vérifier le stock avant d'ajouter au panier
    sql = "SELECT stock FROM Chaussure WHERE id_chaussure = %s"
    mycursor.execute(sql, (id_chaussure,))
    chaussure = mycursor.fetchone()
    date_ajout = datetime.date.today()

    if chaussure and chaussure['stock'] >= quantite:
        print("yes")
        # Ajouter au panier ou mettre à jour la quantité si l'article est déjà présent

        # Étape 1: Vérifier l'existence de l'article dans le panier
        sql_existence = "SELECT id_ligne FROM Ligne_panier WHERE id_utilisateur = %s AND id_chaussure = %s"
        mycursor.execute(sql_existence, (id_client, id_chaussure))
        existing_entry = mycursor.fetchone()

        # Étape 2 et 3: Mise à jour ou insertion basée sur l'existence
        if existing_entry:
            # L'article existe, mise à jour de la quantité
            sql_update = "UPDATE Ligne_panier SET quantite = quantite + %s, date_ajout = %s WHERE id_utilisateur = %s AND id_chaussure = %s"
            mycursor.execute(sql_update, (quantite, date_ajout, id_client, id_chaussure))
        else:
            # L'article n'existe pas, insertion d'un nouvel article
            sql_insert = "INSERT INTO Ligne_panier (quantite, date_ajout, id_utilisateur, id_chaussure) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql_insert, (quantite, date_ajout, id_client, id_chaussure))

        db.commit()
        # retirer du stock
        sql = """
    UPDATE Chaussure
    SET stock = stock - %s
    WHERE  id_chaussure=%s ;
        """
        mycursor.execute(sql, (quantite, id_chaussure))
        db.commit()
        flash('Article ajouté au panier avec succès.', 'success')
    else:
        flash('Stock insuffisant pour cet article.', 'warning')

    return redirect('/client/article/show')






@client_panier.route('/client/panier/delete', methods=['POST'])
def client_panier_delete():
    id_client = session['id_user']
    id_chaussure = request.form.get('id_chaussure')
    quantite = request.form.get('quantite', 1, type=int)
    mycursor = get_db().cursor()


    # partie 2 : on supprime une déclinaison de l'article
    # id_declinaison_article = request.form.get('id_declinaison_article', None)

    sql_existence = """SELECT 
    id_ligne AS IdLigne
    ,quantite as Quantite
    ,date_ajout as DateAjout
    ,id_utilisateur as Idutilisateur
    ,id_chaussure as IdChaussure 
    FROM Ligne_panier WHERE id_utilisateur = %s AND id_chaussure = %s"""
    mycursor.execute(sql_existence, (id_client, id_chaussure))
    article_panier = mycursor.fetchone()

    if not (article_panier is None) and article_panier['Quantite'] > 1:
        # Si la quantité de l'article est supérieure à 1, décrémentez-la de 1
        sql = "UPDATE Ligne_panier SET quantite = quantite - 1 WHERE id_utilisateur = %s AND id_chaussure = %s"
        mycursor.execute(sql, (id_client, id_chaussure))
        flash('Une unité de l\'article a été retirée du panier.', 'success')
    else:
        # Si la quantité est à 1, supprimez l'article du panier
        sql = "DELETE FROM Ligne_panier WHERE id_utilisateur = %s AND id_chaussure = %s"
        mycursor.execute(sql, (id_client, id_chaussure))
        flash('L\'article a été supprimé du panier.', 'success')

    # mise à jour du stock de l'article disponible
    sql = """
    UPDATE Chaussure
    SET stock = stock + %s
    WHERE  id_chaussure=%s ;
        """
    mycursor.execute(sql, (quantite, id_chaussure))

    get_db().commit()
    return redirect('/client/article/show')


@client_panier.route('/client/panier/vider', methods=['POST'])
def client_panier_vider():
    id_client = session['id_user']
    mycursor = get_db().cursor()
    sql = """SELECT 
   id_ligne as IdLigne, 
   quantite as Quantite, 
   date_ajout as DateAjout, 
   id_utilisateur as IdUtilisateur, 
   id_chaussure as IdChaussure 
FROM Ligne_panier 
WHERE id_utilisateur = %s;
"""
    mycursor.execute(sql, (id_client))
    items_panier = mycursor.fetchall()
    print("e",items_panier)
    for items_panier in items_panier:
        id_chaussure= items_panier['IdChaussure']

        sql = ''' DELETE FROM Ligne_panier WHERE id_utilisateur = %s AND id_chaussure = %s'''
        mycursor.execute(sql, (id_client, id_chaussure))

        quantite = items_panier['Quantite']
        sql = """
            UPDATE Chaussure
            SET stock = stock + %s
            WHERE  id_chaussure=%s ;
                """
        mycursor.execute(sql, (quantite, id_chaussure))
        get_db().commit()
    return redirect('/client/article/show')


@client_panier.route('/client/panier/delete/line', methods=['POST'])
def client_panier_delete_line():
    id_client = session['id_user']
    id_chaussure = request.form.get('id_chaussure')
    mycursor = get_db().cursor()
    sql= """SELECT 
           id_ligne AS IdLigne
           ,quantite as Quantite
           ,date_ajout as DateAjout
           ,id_utilisateur as Idutilisateur
           ,id_chaussure as IdChaussure 
           FROM Ligne_panier WHERE id_utilisateur = %s AND id_chaussure = %s"""
    mycursor.execute(sql, (id_client, id_chaussure))
    items_panier = mycursor.fetchone()
    # id_declinaison_article = request.form.get('id_declinaison_article')

    sql = ''' DELETE FROM Ligne_panier WHERE id_utilisateur = %s AND id_chaussure = %s'''
    mycursor.execute(sql, (id_client, id_chaussure))
    quantite = items_panier['Quantite']
    sql = """
    UPDATE Chaussure
    SET stock = stock + %s
    WHERE  id_chaussure=%s ;
        """
    mycursor.execute(sql, (quantite, id_chaussure))

    get_db().commit()
    return redirect('/client/article/show')


@client_panier.route('/client/panier/filtre', methods=['POST'])
def client_panier_filtre():
    # test des variables puis
    # mise en session des variables
    mycursor = get_db().cursor()
    filtre_mot = request.form.get('filtre_mot', None)
    filtre_min = request.form.get('filtre_min', None)
    filtre_max = request.form.get('filtre_max', None)
    filter_types = request.form.getlist('filter_types', None)


    if filtre_mot and filtre_mot != "":
        if len(filtre_mot) > 1:
            if filtre_mot.isalpha():
                session['filtre_mot'] = filtre_mot
            else:
                flash(u'votre mot recherché doit uniquement contenir des lettres')
        else:
            if len(filtre_mot == 1):
                flash(u'votre mot rechercher doit etre plus grand')
            else:
                session.pop('filtre_mot', None)
    if filtre_min or filtre_max:
        if filtre_min.isdecimal() and filtre_max.isdecimal():
            if int(filtre_min) < int(filtre_max):
                session['filtre_min'] = filtre_min
                session['filtre_max'] = filtre_max
                message = u'filtre entre : ' + filtre_min + ' et ' + filtre_max
                flash(message, 'alert-success')
            else:
                message = 'min < max'
                flash(message, 'alert-warning')
        else:
            message = 'pas numerique'
            flash(message, 'alert-warning')
    if filter_types and filter_types != []:
        session['filter_types'] = filter_types
        message = 'case selectioner : '
        for case in filter_types:
            message += 'id:' + case + ' '
        flash(message, 'alert-success')




    return redirect('/client/article/show')















@client_panier.route('/client/panier/filtre/suppr', methods=['POST'])
def client_panier_filtre_suppr():
    # suppression  des variables en session
    session.pop('filtre_mot', None)
    session.pop('filtre_min', None)
    session.pop('filtre_max', None)
    session.pop('filter_types', None)
    print("suppr filtre")
    return redirect('/client/article/show')
