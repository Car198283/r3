# Emissor de  fatura (empresa Sobel)


Sistema web leve e autônomo para criação e impressão de faturas no padrão brasileiro, desenvolvido para a empresa **SOBEL Indústria e Distribuição de Alimentos LTDA**.  
Permite adicionar itens, calcular totais automaticamente, controlar numeração sequencial e gerar PDF para impressão

# Ffuncionalidades

** Pré- visualizaação em tempo real **
    -todos os campos atualizam a fatura instantaneamente.
** Gereciamento dee  itens**
    -adicione, remova e  edite  produtos com quantidade, descrição e preçoo unitário.
** Cálculos automáticos ** 
    – subtotal, impostos, frete e total geral.         
** Subtotal manual opcional **
    – permite sobrescrever o cálculo automático quando necessário.
** Numeração sequencial ** 
    – botão "Próxima numeração" incrementa automaticamente  (ex: `017/26 → 018/26`).    
** Persistência local ** 
    – salva o último número emitido e o rascunho atual no   `localStorage`.
** Impressão / PDF ** 
    – layout otimizado para papel A4 com estilos específicos para impressão.
** Design responsivo ** 
    – funciona bem em desktops, tablets e smartphones.
** Marca d'água decorativa **
   – logo "Sobel" em segundo plano na fatura.



##  Tecnologias utilizadas

- **HTML5** – estrutura semântica
- **CSS3** – design responsivo, flexbox/grid, animações suaves
- **JavaScript (Vanilla)** – manipulação do DOM, lógica de negócio, armazenamento local

Nenhuma dependência externa ou framework – basta abrir o arquivo no navegador.
