# Atividade Pratica: Arquitetura de Software - Modelo MVC

Este repositório apresenta a implementação de um MVP (Produto Mínimo Viável) de uma livraria virtual, desenvolvido para a disciplina de Engenharia de Software. O projeto foca na transição de um sistema simples para uma arquitetura organizada sob o padrão MVC (Model-View-Controller).

## 1. Definição do MVP (Priorização)

A primeira etapa do design consistiu na definição das funcionalidades essenciais através da matriz de Esforço x Resultado. O foco inicial foi estabelecido em funcionalidades de baixo esforço e alto resultado, como a pesquisa global e a vitrine de livros.



## 2. Modelo de Arquitetura Escolhido: MVC

A arquitetura implementada segue o padrão MVC, conforme os conceitos de separação de responsabilidades em camadas. Este modelo permite que a lógica de negócios, a interface do usuário e o controle de fluxo funcionem de forma independente.

### Camadas do Sistema

A organização do projeto reflete as camadas teóricas diretamente na sua estrutura de pastas:

* **Model (Modelo):** Responsável pelo gerenciamento dos dados e das regras de negócio. No projeto, o arquivo `livro_model.py` simula o banco de dados e contém a lógica de filtragem e busca por título, autor ou categoria.
* **View (Visão):** Camada de interação com o usuário. Utiliza templates HTML para renderizar as informações processadas, garantindo que o design seja independente das regras do sistema.
* **Controller (Controlador):** Atua como intermediário. Ele recebe as requisições do usuário via rotas, solicita os dados necessários ao Model e decide qual View será exibida como resposta.

<img width="557" height="373" alt="image" src="https://github.com/user-attachments/assets/7da56336-f3ae-456d-84e9-33c461f34532" />


## 3. Estrutura de Pastas e Organização

A implementação prática no ambiente de desenvolvimento foi organizada para garantir a manutenção e escalabilidade do software, seguindo a hierarquia abaixo:

```text
EX-LAB05/
├── controllers/       # Lógica de controle e rotas (Application)
│   └── livro_controller.py
├── models/            # Lógica de dados e regras (Business/Domain)
│   └── livro_model.py
├── views/             # Interface do usuário (Presentation)
│   └── index.html
└── app.py             # Ponto de entrada da aplicação

```

## FRONT FUNCIONAL:

<img width="1023" height="498" alt="image" src="https://github.com/user-attachments/assets/eb674add-a9e2-499b-8d22-a74a3a4fa0f4" /></br>

<img width="1023" height="488" alt="image" src="https://github.com/user-attachments/assets/256d5ef2-f480-4276-a398-8dcd6d44895f" /></br>

<img width="1024" height="495" alt="image" src="https://github.com/user-attachments/assets/5da4ef2d-6386-45a4-95d6-bc4d2c98a6d7" /></br>


