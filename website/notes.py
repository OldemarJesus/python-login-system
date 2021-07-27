from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
import flask_login
from . import db
from .models import Note
from flask_login import login_required,current_user

notes = Blueprint('notes', __name__)

@notes.route('/', methods=['GET', 'POST'])
@login_required
def start():
    # carrega as notas da base de dados
    notesData = Note.query.filter_by(user_id=current_user.id)

    if request.method == 'POST':
        nota = request.form.get('nota')

        if len(nota) < 3:
            flash('A nota não pode conter menos de 3 caracteres!', category='error')
        else:
            new_note = Note(user_id = current_user.id, description = nota)
            db.session.add(new_note)
            db.session.commit()
            flash('Nota guardada!', category='success')

    return render_template("home.html", user=current_user, notesData = notesData)

@notes.route('/delete-note', methods=['POST'])
@login_required
def delete():
    # elimina a  nota da base de dados
    note_id = request.form.get('id')
    note = Note.query.get(note_id)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('A nota foi eliminada!', category='success')
        else:
            flash('Não foi possível eliminar a nota. Ação não autorizada!', category='error')
    else:
        flash('Nota não encontrada!', category='error')
            
    return redirect(url_for('notes.start'))

