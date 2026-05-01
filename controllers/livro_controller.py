from flask import Blueprint, render_template, request
from models.livro_model import buscar_livros

# Criamos um Blueprint (uma forma do Flask organizar controllers separados)
# Indicamos que a pasta de HTMLs (templates) é a pasta 'views'
livro_bp = Blueprint('livro_bp', __name__, template_folder='../views')


@livro_bp.route('/', methods=['GET', 'POST'])
def index():
    termo = ""

    # Se o usuário clicou no botão "Pesquisar" (POST)
    if request.method == 'POST':
        termo = request.form.get('termo_busca', '')

    # Pede para o MODEL processar a busca
    livros_filtrados = buscar_livros(termo)

    # Envia os dados de volta para a VIEW
    return render_template('index.html', livros=livros_filtrados, termo_pesquisado=termo)