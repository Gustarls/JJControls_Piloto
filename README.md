# J&JControls

**J&JControls** é um sistema desktop de controle de estoque com foco em rastreabilidade de produtos defeituosos, movimentações internas e análise gráfica de falhas. Ele foi desenvolvido com Python, utilizando interface gráfica com Tkinter e visualizações com Plotly.

## 🧰 Funcionalidades

- Cadastro completo de produtos reprovados com foto, técnico responsável e tipo de defeito
- Registro de movimentações de entrada e saída por produto
- Histórico de operações com filtros por usuário e data
- Exportação de relatórios em Excel (produtos, movimentações e log de operações)
- Visualização de gráficos interativos:
  - Reprovas por data (semana ou mês)
  - Reprovas por turno
  - Tipo de defeito x Tag (INDEX/PIDM)
  - Volume total por Tag (gráfico de pizza)

## 💻 Tecnologias utilizadas

- Python 3.x
- Tkinter (interface gráfica)
- SQLite (banco de dados local)
- Pandas
- Plotly
- OpenPyXL (exportação em Excel)
- Pillow (para manipulação de imagens)
- Kaleido (para exportação de gráficos)

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/jjcontrols.git
cd jjcontrols
pip install -r requirements.txt
```

> Certifique-se de ter o Python 3 instalado na máquina.

## ▶️ Como usar

Execute o arquivo principal:

```bash
python JJS_Piloto.py
```

O sistema abrirá uma tela de login, seguida da interface principal com abas de cadastro, movimentações, histórico e gráficos.

Login: admin
Senha admin123

## 📁 Estrutura esperada

- `JJS_Piloto.py` — Script principal
- `jj_login_module.py` — Módulo com a lógica de login
- `estoque.db` — Banco de dados SQLite (criado automaticamente)
- `fotos_reprovas/` — Pasta onde as imagens de produtos são salvas

## 🔐 Requisitos adicionais

- O módulo `jj_login_module.py` deve conter a função `abrir_login()` para controle de acesso ao sistema.
- A biblioteca Kaleido deve estar instalada corretamente para exportação de gráficos.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar.
