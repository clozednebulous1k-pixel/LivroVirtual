# LivroVirtual

Site de apresentação e venda do devocional **365 Dias de Amor com Deus**: landing em `index.html`, assets em `assets/`. O PDF do livro fica em `entrega/` para você enviar manualmente ao cliente após a compra — a landing **não** oferece download público do arquivo.

Para regenerar o HTML opcional do livro (versão navegador), use Python:

```bash
python tools/build_livro_entrega.py
```

O checkout **Comprar agora** aponta para a Fruitfy Pay em `index.html` (`#lv-checkout`). Altere o `href` se trocar de plataforma.

### Meta Pixel (ID `1371933481506696`)

- Código base e `PageView` no `<head>` ([documentação do Pixel](https://developers.facebook.com/docs/meta-pixel)).
- **ViewContent** (uma vez por carregamento da página) com `content_ids`, `value`, `currency` e **`eventID`** para deduplicação.
- **InitiateCheckout** em cada clique em **Comprar agora**, com **`eventID` único** por clique.
- Para **Purchase** e deduplicação com a API de Conversões (CAPI), use o **mesmo `event_id`** que a Fruitfy enviar no servidor e o documentado em [Deduplicar eventos do Pixel e do servidor](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events). Nesta landing o `Purchase` não é disparado no browser (normalmente só na página de obrigado / webhook).
