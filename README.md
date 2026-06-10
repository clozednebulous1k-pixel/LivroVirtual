# LivroVirtual

Site de apresentação e venda do devocional **365 Dias de Amor com Deus**: landing em `index.html`, assets em `assets/`. O PDF do livro fica em `entrega/` para você enviar manualmente ao cliente após a compra — a landing **não** oferece download público do arquivo.

Para regenerar o HTML opcional do livro (versão navegador), use Python:

```bash
python tools/build_livro_entrega.py
```

Personalize textos em `index.html` e conecte o botão **Comprar agora** (`#lv-checkout`) ao link ou snippet da sua gateway de pagamento.
