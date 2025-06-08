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
- PIL (exibição de imagens)
- Kaleido (exportação de gráficos como JPEG)

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/jjcontrols.git
cd jjcontrols
pip install -r requirements.txt
