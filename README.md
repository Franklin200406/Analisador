# Analisador Lexico da LPN

Este projeto implementa um analisador léxico em Python para a linguagem procedural **LPN (Linguagem Procedural Nobre)**, utilizando a biblioteca `re` e expressoes regulares.

O programa le um codigo-fonte escrito em LPN, converte esse codigo em tokens e gera um arquivo HTML com o resultado da analise. Quando existe algum erro lexico, o HTML passa a exibir a mensagem de erro com a linha e a coluna correspondentes.

## Objetivo do projeto

O objetivo deste trabalho e:

- reconhecer lexemas válidos da linguagem LPN;
- transformar a entrada em uma lista de tokens no formato `(TIPO_TOKEN, valor)`;
- ignorar espacos em branco e comentarios;
- detectar simbolos invalidos e informar erro lexico;
- gerar um arquivo HTML com a tabela de simbolos ou com a mensagem de erro.

## Estrutura dos arquivos

Os arquivos essenciais do projeto são:

- `definicao_linguagem_lpn.md`
  Arquivo com a definicao da linguagem, contendo palavras-chave, operadores, delimitadores e regex utilizadas.

- `codigo_exemplo.lpn`
  Arquivo de entrada. E nele que o codigo LPN deve ser escrito para ser analisado.

- `lexer_lpn.py`
  Implementacao do analisador léxico em Python.

- `.vscode/launch.json`
  Configuracao para executar o projeto diretamente no VS Code com `F5`.

## Requisitos para execucao

Para executar o projeto, e necessario ter:

- Python 3 instalado no computador
- VS Code instalado
- extensao `Python` da Microsoft instalada no VS Code

## Como executar no VS Code

Siga exatamente estes passos:

1. Abra o VS Code.

2. No VS Code, escolha `File > Open Folder`.

3. Abra a pasta do projeto:

```text
C:\Users\enzof\OneDrive\Documentos\Analisador
```

4. No painel lateral do VS Code, abra o arquivo `codigo_exemplo.lpn`.

5. Escreva ou edite o codigo LPN que deseja analisar.

6. Se for a primeira execucao, selecione o interpretador do Python:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

7. Escolha o Python instalado na maquina.

8. Abra o arquivo `lexer_lpn.py`.

9. Pressione `F5` para executar o analisador.

10. Se o VS Code solicitar uma configuracão de execucão, selecione:

```text
Executar Lexer LPN
```

11. Aguarde a execucão terminar.

12. Apos a execucao, abra o arquivo:

```text
resultado_analise_lexica.html
```

Esse arquivo sera criado ou atualizado automaticamente pelo programa.

## Onde escrever o codigo que sera analisado

O codigo de entrada deve ser escrito em:

```text
codigo_exemplo.lpn
```

Tudo o que estiver nesse arquivo sera lido pelo analisador lexico.

## Onde o resultado aparece

O resultado da analise aparece em:

```text
resultado_analise_lexica.html
```

Esse arquivo pode apresentar dois cenarios:

- **Sucesso**
  Mostra o status da analise e a tabela de simbolos com os tokens reconhecidos.

- **Erro lexico**
  Mostra uma mensagem informando o simbolo invalido encontrado e a posicao aproximada no codigo, com linha e coluna.

## Exemplo de uso

Exemplo de codigo valido em `codigo_exemplo.lpn`:

```text
inteiro x;
x = 10;
```

Exemplo esperado de tokens:

```text
('INTEIRO', 'inteiro')
('ID', 'x')
('PONTO_VIRGULA', ';')
('ID', 'x')
('ATRIBUICAO', '=')
('NUM_INT', '10')
('PONTO_VIRGULA', ';')
```

## Como testar erro lexico

Para verificar se o analisador detecta erro lexico, escreva um simbolo invalido no arquivo `codigo_exemplo.lpn`, por exemplo:

```text
inteiro x;
@
```

Depois execute novamente com `F5`.

O arquivo `resultado_analise_lexica.html` devera exibir uma mensagem semelhante a:

```text
Simbolo invalido encontrado: '@' (linha 2, coluna 1)
```

## O que cada arquivo faz

### `definicao_linguagem_lpn.md`

Documenta formalmente os elementos da linguagem reconhecidos pelo lexer:

- palavras-chave;
- identificadores;
- numeros inteiros e reais;
- strings;
- operadores;
- delimitadores;
- comentarios.

### `codigo_exemplo.lpn`

Representa a entrada do analisador. Este arquivo existe para separar claramente:

- a definicao da linguagem;
- o codigo fonte de exemplo;
- a implementacao do analisador.

### `lexer_lpn.py`

Este arquivo:

- le o conteudo de `codigo_exemplo.lpn`;
- tokeniza o conteudo com expressoes regulares;
- ignora comentarios e espacos em branco;
- detecta erro lexico;
- gera o arquivo `resultado_analise_lexica.html`.

## Observacoes importantes para avaliacao

- O projeto foi organizado para que a avaliacao possa ser feita diretamente no VS Code.
- Nao e necessario editar o codigo Python para testar novas entradas.
- Basta alterar `codigo_exemplo.lpn`, executar `lexer_lpn.py` com `F5` e abrir o HTML gerado.
- O HTML final serve como evidência visual do resultado da analise.