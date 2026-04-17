import html
import re
import sys
from pathlib import Path


# ============================================================================
# PARTE 2 - ANALISADOR LEXICO DA LPN
# Este arquivo contem toda a implementacao do lexer.
# O codigo que sera analisado deve ser escrito em "codigo_exemplo.lpn".
# A definicao resumida da linguagem esta em "definicao_linguagem_lpn.md".
# ============================================================================


class ErroLexico(Exception):
    """Erro levantado quando um lexema invalido e encontrado."""

    def __init__(self, mensagem: str, linha: int, coluna: int):
        super().__init__(f"{mensagem} (linha {linha}, coluna {coluna})")
        self.linha = linha
        self.coluna = coluna


class AnalisadorLexicoLPN:
    """Lexer da Linguagem Procedural Nobre (LPN)."""

    PALAVRAS_CHAVE = {
        "inteiro": "INTEIRO",
        "real": "REAL",
        "texto": "TEXTO",
        "se": "SE",
        "senao": "SENAO",
        "enquanto": "ENQUANTO",
        "para": "PARA",
        "funcao": "FUNCAO",
        "procedimento": "PROCEDIMENTO",
        "retorne": "RETORNE",
        "escolha": "ESCOLHA",
        "caso": "CASO",
        "padrao": "PADRAO",
        "pare": "PARE",
        "continue": "CONTINUE",
    }

    ESPECIFICACAO_TOKENS = [
        ("COMENTARIO_BLOCO", r"/\*[\s\S]*?\*/"),
        ("COMENTARIO_LINHA", r"//[^\n]*"),
        ("STRING", r'"(?:\\.|[^"\\])*"'),
        ("NUM_REAL", r"\d+\.\d+"),
        ("NUM_INT", r"\d+"),
        ("E_LOGICO", r"&&"),
        ("OU_LOGICO", r"\|\|"),
        ("MAIOR_IGUAL", r">="),
        ("MENOR_IGUAL", r"<="),
        ("IGUAL", r"=="),
        ("DIFERENTE", r"!="),
        ("ATRIBUICAO", r"="),
        ("MAIOR", r">"),
        ("MENOR", r"<"),
        ("NEGACAO", r"!"),
        ("MAIS", r"\+"),
        ("MENOS", r"-"),
        ("MULT", r"\*"),
        ("DIV", r"/"),
        ("MOD", r"%"),
        ("PONTO_VIRGULA", r";"),
        ("VIRGULA", r","),
        ("DOIS_PONTOS", r":"),
        ("ABRE_PAREN", r"\("),
        ("FECHA_PAREN", r"\)"),
        ("ABRE_CHAVE", r"\{"),
        ("FECHA_CHAVE", r"\}"),
        ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
        ("ESPACO", r"[ \t\r\n]+"),
        ("INVALIDO", r"."),
    ]

    def __init__(self):
        partes = [f"(?P<{nome}>{padrao})" for nome, padrao in self.ESPECIFICACAO_TOKENS]
        self.regex_master = re.compile("|".join(partes))

    def tokenizar(self, codigo_fonte: str):
        tokens = []
        linha = 1
        coluna = 1

        for correspondencia in self.regex_master.finditer(codigo_fonte):
            tipo = correspondencia.lastgroup
            valor = correspondencia.group(tipo)
            linha_atual = linha
            coluna_atual = coluna

            if tipo == "INVALIDO":
                raise ErroLexico(
                    f"Simbolo invalido encontrado: {valor!r}",
                    linha_atual,
                    coluna_atual,
                )

            if tipo not in {"ESPACO", "COMENTARIO_LINHA", "COMENTARIO_BLOCO"}:
                if tipo == "ID" and valor in self.PALAVRAS_CHAVE:
                    tipo = self.PALAVRAS_CHAVE[valor]
                tokens.append((tipo, valor))

            qtd_quebras = valor.count("\n")
            if qtd_quebras:
                linha += qtd_quebras
                coluna = len(valor.rsplit("\n", 1)[-1]) + 1
            else:
                coluna += len(valor)

        self._validar_trechos_nao_reconhecidos(codigo_fonte)
        return tokens

    def _validar_trechos_nao_reconhecidos(self, codigo_fonte: str):
        """Detecta comentario de bloco nao encerrado."""
        abertura = codigo_fonte.find("/*")
        while abertura != -1:
            fechamento = codigo_fonte.find("*/", abertura + 2)
            if fechamento == -1:
                trecho = codigo_fonte[:abertura]
                linha = trecho.count("\n") + 1
                coluna = len(trecho.rsplit("\n", 1)[-1]) + 1
                raise ErroLexico("Comentario de bloco nao encerrado", linha, coluna)
            abertura = codigo_fonte.find("/*", fechamento + 2)


def gerar_tabela_html(tokens, caminho_saida: str):
    """Gera um arquivo HTML com a tabela de simbolos."""
    linhas_tabela = []
    for tipo, valor in tokens:
        linhas_tabela.append(
            "        <tr>"
            f"<td>{html.escape(tipo)}</td>"
            f"<td>{html.escape(valor)}</td>"
            "</tr>"
        )

    conteudo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabela de Simbolos - LPN</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f4f6f8;
            color: #1f2933;
        }}
        .secao {{
            margin-bottom: 28px;
            padding: 20px;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }}
        h1 {{
            margin-bottom: 20px;
        }}
        h2 {{
            margin-top: 0;
        }}
        .sucesso {{
            color: #166534;
            font-weight: bold;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #d9e2ec;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background: #102a43;
            color: #ffffff;
        }}
        tr:nth-child(even) {{
            background: #f8fbff;
        }}
    </style>
</head>
<body>
    <h1>Resultado da Analise Lexica da LPN</h1>

    <section class="secao">
        <h2>Status da Analise</h2>
        <p class="sucesso">Analise concluida com sucesso. Nenhum erro lexico foi encontrado.</p>
    </section>

    <section class="secao">
        <h2>Tabela de Simbolos</h2>
        <table>
            <thead>
                <tr>
                    <th>Tipo do Token</th>
                    <th>Valor</th>
                </tr>
            </thead>
            <tbody>
{chr(10).join(linhas_tabela)}
            </tbody>
        </table>
    </section>
</body>
</html>
"""

    Path(caminho_saida).write_text(conteudo, encoding="utf-8")


def gerar_erro_html(caminho_saida: str, mensagem_erro: str):
    """Gera um arquivo HTML informando o erro lexico encontrado."""
    conteudo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erro Lexico - LPN</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #fef2f2;
            color: #7f1d1d;
        }}
        .secao {{
            padding: 20px;
            background: #ffffff;
            border-left: 6px solid #dc2626;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }}
        code {{
            font-size: 1rem;
        }}
    </style>
</head>
<body>
    <h1>Resultado da Analise Lexica da LPN</h1>
    <section class="secao">
        <h2>Erro Lexico Encontrado</h2>
        <p>O codigo exemplo possui um erro lexico e nao foi possivel gerar a tabela de simbolos.</p>
        <p><code>{html.escape(mensagem_erro)}</code></p>
    </section>
</body>
</html>
"""

    Path(caminho_saida).write_text(conteudo, encoding="utf-8")


def carregar_codigo_fonte():
    """
    Carrega o codigo LPN a partir de um arquivo.
    Se nenhum caminho for informado, usa o arquivo codigo_exemplo.lpn na mesma pasta.
    """
    base_dir = Path(__file__).resolve().parent
    caminho_entrada = Path(sys.argv[1]) if len(sys.argv) > 1 else base_dir / "codigo_exemplo.lpn"
    return caminho_entrada.resolve(), caminho_entrada.read_text(encoding="utf-8")


def main():
    analisador = AnalisadorLexicoLPN()
    base_dir = Path(__file__).resolve().parent
    arquivo_saida = base_dir / "resultado_analise_lexica.html"

    try:
        caminho_entrada, codigo_fonte = carregar_codigo_fonte()
        tokens = analisador.tokenizar(codigo_fonte)
        print("Tokens reconhecidos:")
        for token in tokens:
            print(token)

        gerar_tabela_html(tokens, str(arquivo_saida))
        print(f"\nArquivo analisado: {caminho_entrada}")
        print(f"Resultado HTML gerado em: {arquivo_saida}")
    except FileNotFoundError as erro:
        print(f"Arquivo de entrada nao encontrado: {erro.filename}")
    except ErroLexico as erro:
        gerar_erro_html(str(arquivo_saida), str(erro))
        print(f"Erro lexico: {erro}")
        print(f"Resultado HTML gerado em: {arquivo_saida}")


if __name__ == "__main__":
    main()
