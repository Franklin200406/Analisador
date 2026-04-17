# PARTE 1 - DEFINICAO DA LINGUAGEM LPN

Este arquivo documenta, de forma organizada, os elementos que o analisador lexico reconhece.

## Palavras-chave

- `inteiro`
- `real`
- `texto`
- `se`
- `senao`
- `enquanto`
- `para`
- `funcao`
- `procedimento`
- `retorne`
- `escolha`
- `caso`
- `padrao`
- `pare`
- `continue`

## Identificadores

Regex reconhecida:

```text
[a-zA-Z_][a-zA-Z0-9_]*
```

## Numeros

Regex reconhecidas:

```text
\d+
\d+\.\d+
```

## Strings

Textos entre aspas duplas:

```text
"exemplo"
```

## Operadores aritmeticos

- `+`
- `-`
- `*`
- `/`
- `%`

## Operadores logicos

- `&&`
- `||`
- `!`

## Operadores de comparacao

- `>`
- `<`
- `>=`
- `<=`
- `==`
- `!=`
- `=`

## Delimitadores

- `;`
- `,`
- `:`
- `(`
- `)`
- `{`
- `}`

## Comentarios ignorados pelo lexer

- Linha: `// comentario`
- Bloco: `/* comentario */`

## Organizacao do projeto

- [definicao_linguagem_lpn.md](C:\Users\enzof\OneDrive\Documentos\New project\definicao_linguagem_lpn.md): definicao da linguagem
- [codigo_exemplo.lpn](C:\Users\enzof\OneDrive\Documentos\New project\codigo_exemplo.lpn): arquivo para voce escrever o codigo de entrada
- [lexer_lpn.py](C:\Users\enzof\OneDrive\Documentos\New project\lexer_lpn.py): analisador lexico em Python
- [resultado_analise_lexica.html](C:\Users\enzof\OneDrive\Documentos\New project\resultado_analise_lexica.html): saida gerada apos a execucao
