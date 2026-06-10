# LivroVirtual

Site de apresentação e venda do devocional **365 Dias de Amor com Deus**: landing em `index.html`, assets em `assets/`. O PDF do livro fica em `entrega/` para você enviar manualmente ao cliente após a compra — a landing **não** oferece download público do arquivo.

Para regenerar o HTML opcional do livro (versão navegador), use Python:

```bash
python tools/build_livro_entrega.py
```

O checkout **Comprar agora** aponta para a Fruitfy Pay em `index.html` (`#lv-checkout`). Altere o `href` se trocar de plataforma.
