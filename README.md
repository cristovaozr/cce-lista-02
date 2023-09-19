# Lista 02 - Códigos Corretores de Erro

Este repositótio contém as soluções que eu fiz para as questões da Lista 02 da disciplina de Códigos Corretores de Erro da UFPE 2023.2.

As soluções estão escritas nas seguintes linguages de programação
* Python3

## Preparando o ambiente para execução

Para executar é necessário iniciar o ambiente virtual e instalar as dependências:

```bash
$ python3 -m venv venv     # Inicia um virtual env (venv) na pasta "venv"
$ source venv/bin/activate # Ativa o ambiente virtual
(venv) $ pip install -r requirements.txt # Instala as dependências
```

Depois de instalar as dependências os arquivos das questões estão prontos para serem utilizados!

## Execução das soluções disponíveis

Para iniciar a execução dos arquivos é necessário inicializar o _virtual env_:

```bash
$ source venv/bin/activate
(venv) $ # Agora pode executar o programa em Python!
```

Para desativar o ambiente basta fazer:

```bash
(venv) $ deactivate
$ # Agora o virtual env está desativado!
```

Todos os arquivos são executáveis. Para tanto basta invocá-los diretamente do shell do Linux ou usar sua ferramenta Python de preferência:
```bash
$ ./questao-2.10.py       # Primeira opção
$ python3 questao-2.10.py # Segunda opção
```

## Resumo das soluções das questões

### Questão 2.10
O arquivo `questao-2.10.py` contém um código que ajudou a se o polinômio x⁵+x³+1 é irredutível no GF(2)

### Questão 2.12
O arquivo `questao-2.12.py` determina todos os polinômios de grau 5 que são irredutíveis no GF(2)