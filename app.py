import datetime
from flask import Flask, render_template, request, flash, redirect, url_for

from models import db_session, Funcionario
from sqlalchemy import select
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = 'senai_terapia_sp'

@app.route('/')
def home():
    return render_template("funcionarios.html")

@app.route('/funcionarios')
def funcionarios():
    funcionarios_sql = select(Funcionario)
    funcionarios_resultado = db_session.execute(funcionarios_sql).scalars().all()

    return render_template("funcionarios.html", lista_funcionarios=funcionarios_resultado)

@app.route('/funcionarios', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        if (request.form['form-nome'] and request.form['form-data-nasc'] and request.form['form-cpf'] and request.form['form-email'] and
                request.form['form-senha'] and request.form['form-cargo'] and request.form['form-salario']):

            nome = request.form['form-nome']
            data_nasc = datetime.datetime.strptime(request.form['form-data-nasc'], "%Y-%m-%d")
            cpf = request.form['form-cpf']
            email = request.form['form-email']
            senha = request.form['form-senha']
            cargo = request.form['form-cargo']
            salario = float(request.form['form-salario'])


            user_email = select(Funcionario).where(Funcionario.email == email)
            user_email = db_session.execute(user_email).scalars().one_or_none()

            if user_email:
                flash("Usuário ja existe", 'alert-danger')
            else:
                funcionario = Funcionario(nome=nome, data_nascimento=data_nasc,
                                          cpf=cpf ,email=email, cargo=cargo, salario=salario)
                funcionario.set_password(senha)
                db_session.add(funcionario)
                db_session.commit()
                db_session.close()
        else:
            flash("Preencha todos os campos", 'alert-danger')


        return redirect(url_for('funcionarios'))
    return redirect(url_for('funcionarios'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
