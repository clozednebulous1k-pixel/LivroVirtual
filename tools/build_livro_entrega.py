# -*- coding: utf-8 -*-
"""Gera entrega/365-Dias-de-Amor-com-Deus.html — livro virtual único (layout open-book)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "open-book.css").read_text(encoding="utf-8")
INTRO = (ROOT / "tools" / "introducao_fragment.html").read_text(encoding="utf-8")
OUT = ROOT / "entrega" / "365-Dias-de-Amor-com-Deus.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

MESES = [
    ("Janeiro", 31),
    ("Fevereiro", 28),
    ("Março", 31),
    ("Abril", 30),
    ("Maio", 31),
    ("Junho", 30),
    ("Julho", 31),
    ("Agosto", 31),
    ("Setembro", 30),
    ("Outubro", 31),
    ("Novembro", 30),
    ("Dezembro", 31),
]


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def amostra_dia(n: int) -> dict:
    """Alguns dias com texto de exemplo; demais usam modelo editável."""
    if n == 1:
        return {
            "titulo": "Começo suave",
            "ref": "Salmo 23:1–3 (ideia)",
            "p1": "Deus não exige que você chegue inteiro para começar. Ele pede presença — e presença pode ser pequena, como uma vela acesa num quarto escuro.",
            "p2": "Hoje, respire fundo uma vez. Diga, em silêncio: “Tu és meu pastor.” Deixe a frase descansar no corpo, não só na cabeça.",
            "p3": "Se a mente fugir, não leve culpa. Volte. Amor com Deus é dança de idas e vindas, não prova de desempenho.",
            "pergunta": "Onde você mais sente necessidade de descanso hoje?",
        }
    if n == 2:
        return {
            "titulo": "Escuta antes da solução",
            "ref": "Tiago 1:19 (ideia)",
            "p1": "Às vezes oramos correndo: pedimos, planejamos, resolvemos — e quase não sobra espaço para ouvir.",
            "p2": "Que este dia tenha um minuto em que você não peça nada. Apenas fique ali, como filho ao lado do Pai.",
            "p3": "A fé madura aprende que nem todo silêncio é abandono; às vezes é convite.",
            "pergunta": "Que barulho interno você pode abaixar um pouco para ouvir melhor?",
        }
    if n == 3:
        return {
            "titulo": "Graça para recomeçar",
            "ref": "Lamentações 3:22–23 (ideia)",
            "p1": "Se ontem foi difícil, a misericórdia de Deus não ficou presa no calendário de ontem. Ela se renova.",
            "p2": "Recomeçar não é fracasso espiritual; é honrar a vida que ainda está em suas mãos.",
            "p3": "Escreva mentalmente um “sim” pequeno a Deus hoje — não um projeto enorme, um passo verdadeiro.",
            "pergunta": "Qual recomeço você precisa aceitar com ternura?",
        }
    return {
        "titulo": f"Dia {n} — seu título aqui",
        "ref": "Referência bíblica (opcional)",
        "p1": f"Substitua este parágrafo pelo texto do dia {n}. Conteúdo exclusivo do seu livro: leitura curta, convite à meditação e tom acolhedor.",
        "p2": "Segundo parágrafo: aprofunde o tema, conte uma imagem simples, conecte o cotidiano com a presença de Deus.",
        "p3": "Terceiro parágrafo: feche com esperança prática — algo que a pessoa possa levar até a noite.",
        "pergunta": "Pergunta do dia para diário ou oração (edite no arquivo ou substitua pela versão final).",
    }


def montar_article(n: int) -> str:
    d = amostra_dia(n)
    tit = esc(d["titulo"])
    ref = esc(d["ref"])
    return f"""<h2 class="chapter-title">{tit}</h2>
            <p><strong>Leitura sugerida:</strong> {ref}</p>
            <p>{esc(d["p1"])}</p>
            <p>{esc(d["p2"])}</p>
            <p>{esc(d["p3"])}</p>
            <hr />
            <p><strong>Pergunta do dia:</strong> {esc(d["pergunta"])}</p>"""


def paginas_spread(n: int) -> tuple[int, int]:
    """Numeração após a introdução (páginas 12–13). Dias: 14–15, 16–17, …"""
    base = 14 + (n - 1) * 2
    return base, base + 1


def bloco_open_book(n: int) -> str:
    a, b = paginas_spread(n)
    art = montar_article(n)
    return f"""
    <section class="open-book spread-dia" id="dia-{n}" data-dia="{n}" aria-label="Dia {n}">
      <header>
        <h1>Dia {n}</h1>
        <h6>365 Dias de Amor com Deus</h6>
      </header>
      <article>
        {art}
      </article>
      <footer>
        <ol class="page-numbers" aria-label="Páginas">
          <li>{a}</li>
          <li>{b}</li>
        </ol>
      </footer>
    </section>"""


# IDs no CSS do site usam #livro-aberto; no livro entregue usamos wrapper .livro-entrega
CSS_ENTREGA = (
    CSS.replace("#livro-aberto", ".livro-entrega-wrap")
    + """

/* Leitor: barra e capa (branco & dourado) */
:root {
  --e-bg: #faf8f4;
  --e-ink: #1c1914;
  --e-gold: #a67c00;
  --e-gold-b: #c9a227;
  --e-border: rgba(166, 124, 0, 0.28);
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body.livro-app {
  margin: 0;
  font-family: "Literata", "Crimson Text", Georgia, serif;
  background: var(--e-bg);
  color: var(--e-ink);
  padding-top: 3.75rem;
}

.reader-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1rem;
  padding: 0.65rem 1rem;
  background: linear-gradient(180deg, #fffdf8, #faf6ef);
  border-bottom: 1px solid var(--e-border);
  box-shadow: 0 4px 20px rgba(166, 124, 0, 0.08);
}

.reader-bar strong {
  font-family: "Fraunces", "Playfair Display", Georgia, serif;
  font-weight: 600;
  color: var(--e-gold);
  letter-spacing: 0.04em;
}

.reader-bar label { font-size: 0.85rem; color: #5c5346; }

.reader-bar input[type="number"] {
  width: 4.5rem;
  padding: 0.35rem 0.5rem;
  border: 1px solid var(--e-border);
  border-radius: 4px;
  font-size: 1rem;
}

.reader-bar button {
  font-family: "Fraunces", Georgia, serif;
  cursor: pointer;
  border: 1px solid var(--e-border);
  background: linear-gradient(180deg, #fff, #f5f0e6);
  color: var(--e-ink);
  padding: 0.4rem 0.85rem;
  border-radius: 4px;
}

.reader-bar button.primary {
  background: linear-gradient(145deg, var(--e-gold-b), var(--e-gold));
  color: #1c1914;
  border-color: rgba(255,255,255,0.35);
  font-weight: 600;
}

.reader-bar a {
  color: var(--e-gold);
  font-size: 0.9rem;
}

.capa-livro {
  max-width: 36rem;
  margin: 2rem auto 2.5rem;
  padding: 2.5rem 2rem;
  text-align: center;
  background: #fff;
  border: 1px solid var(--e-border);
  border-radius: 6px;
  box-shadow: 0 12px 40px rgba(0,0,0,0.06);
}

.capa-livro h1 {
  font-family: "Fraunces", "Playfair Display", Georgia, serif;
  font-weight: 500;
  font-size: clamp(1.75rem, 5vw, 2.5rem);
  margin: 0 0 0.5rem;
  color: var(--e-ink);
}

.capa-livro .sub {
  color: var(--e-gold);
  font-family: "Playfair Display", Georgia, serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-size: 0.75rem;
  margin-bottom: 1.25rem;
}

.capa-livro p { color: #5c5346; line-height: 1.6; margin: 0 0 1rem; }

.livro-entrega-wrap {
  padding: 0 0 3rem;
  background: #ece8df;
}

#bookWrapper { max-width: 80em; margin: 0 auto; }
#bookContainer { width: 100%; padding: 1em; }

.sumario-intro {
  margin: 0 0 1rem;
  padding: 0 0 0.75rem;
  border-bottom: 1px solid var(--e-border);
}
.sumario-intro a {
  font-family: "Fraunces", Georgia, serif;
  font-weight: 600;
  color: var(--e-gold);
  text-decoration: none;
  font-size: 1rem;
}
.sumario-intro a:hover {
  text-decoration: underline;
}

details.sumario {
  max-width: 48rem;
  margin: 0 auto 1.5rem;
  padding: 0 1rem;
}

details.sumario > summary {
  cursor: pointer;
  font-family: "Fraunces", Georgia, serif;
  color: var(--e-gold);
  font-weight: 600;
  padding: 0.5rem 0;
}

.sumario-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 0.35rem;
  margin-top: 0.75rem;
}

.sumario-grid a {
  display: block;
  padding: 0.35rem 0.5rem;
  border-radius: 4px;
  border: 1px solid var(--e-border);
  background: #fff;
  color: var(--e-ink);
  text-decoration: none;
  font-size: 0.85rem;
  text-align: center;
}

.sumario-grid a:hover {
  border-color: var(--e-gold-b);
  color: var(--e-gold);
}

@media print {
  .reader-bar, details.sumario, .capa-livro { display: none !important; }
  body.livro-app { padding-top: 0; }
  .spread-dia { break-after: page; }
}
"""
)

bloques = INTRO.strip() + "\n" + "\n".join(bloco_open_book(n) for n in range(1, 366))

sumario_parts = []
dia_atual = 1
for nome, q in MESES:
    links = []
    for _ in range(q):
        links.append(f'<a href="#dia-{dia_atual}">Dia {dia_atual}</a>')
        dia_atual += 1
    sumario_parts.append(f"<h4>{nome}</h4><div class=\"sumario-grid\">{''.join(links)}</div>")

sumario_intro = '<div class="sumario-intro"><a href="#introducao">Introdução (como usar o livro)</a></div>'
sumario_html = sumario_intro + "\n" + "\n".join(sumario_parts)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="365 Dias de Amor com Deus — livro virtual. Uso pessoal após compra." />
  <title>365 Dias de Amor com Deus — Livro virtual</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..700&family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet" />
  <style>
{CSS_ENTREGA}
  </style>
</head>
<body class="livro-app">
  <nav class="reader-bar" aria-label="Navegação do livro">
    <strong>365 Dias · Amor com Deus</strong>
    <label for="dia-input">Ir para dia</label>
    <input id="dia-input" type="number" min="1" max="365" value="1" aria-label="Número do dia" />
    <button type="button" class="primary" id="btn-ir">Abrir</button>
    <button type="button" id="btn-prev">Anterior</button>
    <button type="button" id="btn-next">Próximo</button>
    <a href="#introducao">Introdução</a>
    <a href="#sumario">Sumário</a>
    <a href="#capa">Capa</a>
  </nav>

  <header class="capa-livro" id="capa">
    <p class="sub">Livro virtual</p>
    <h1>365 Dias de Amor com Deus</h1>
    <p><strong>Livro completo:</strong> introdução em formato de páginas abertas + <strong>365 dias</strong> de encontros. Salve este arquivo no aparelho e abra no navegador (Chrome, Edge, Safari). Funciona offline após carregar uma vez.</p>
    <p style="font-size:0.9rem;color:#8a7e6a">Use a barra acima para ir ao dia, ao sumário, à introdução ou à capa. Para editar textos, use os arquivos em <code>tools/</code> e rode <code>python tools/build_livro_entrega.py</code>.</p>
  </header>

  <details class="sumario" id="sumario" open>
    <summary>Sumário — ir a um dia</summary>
    {sumario_html}
  </details>

  <div class="livro-entrega-wrap">
    <div id="bookWrapper">
      <div id="bookContainer">
{bloques}
      </div>
    </div>
  </div>

  <script>
(function () {{
  var input = document.getElementById("dia-input");
  function go(n) {{
    n = Math.max(1, Math.min(365, parseInt(n, 10) || 1));
    input.value = n;
    var el = document.getElementById("dia-" + n);
    if (el) el.scrollIntoView({{ behavior: "smooth", block: "start" }});
  }}
  document.getElementById("btn-ir").addEventListener("click", function () {{
    go(input.value);
  }});
  document.getElementById("btn-prev").addEventListener("click", function () {{
    go((parseInt(input.value, 10) || 1) - 1);
  }});
  document.getElementById("btn-next").addEventListener("click", function () {{
    go((parseInt(input.value, 10) || 1) + 1);
  }});
  window.addEventListener("hashchange", function () {{
    var m = /^#dia-(\\d+)$/.exec(location.hash);
    if (m) input.value = m[1];
  }});
}})();
  </script>
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print("Gerado:", OUT, "bytes:", OUT.stat().st_size)
