## Triângulo de Floyd

Este script em Python imprime o Triângulo de Floyd com base no número de linhas que o usuário define.

**Descrição**

O Triângulo de Floyd é uma disposição de números naturais em formato triangular, onde a primeira linha contém 1 número, a segunda contém 2 números, a terceira contém 3 números e assim por diante. O script solicita que o usuário insira o número de linhas desejadas e, em seguida, imprime o triângulo com a quantidade correspondente de números.

**Como funciona?**

O script começa pedindo ao usuário para inserir um número de linhas. Se o número for maior que 0, ele irá construir o triângulo. Caso contrário, uma mensagem de erro será exibida.

**Estrutura do Código**
- Entrada do Usuário: O usuário insere o número de linhas do triângulo.
- Verificação da Entrada: O código verifica se o número de linhas é maior que 0. Se for, começa a construção do triângulo; se não for, exibe uma mensagem de erro.
- Construção do Triângulo: O código utiliza dois loops:
  O primeiro loop (for c in range(1, linha + 1)) controla o número de linhas.
  O segundo loop (for j in range(c)) imprime a quantidade certa de números em cada linha.
- A variável num mantém o controle do número atual a ser impresso.
- Impressão: Para cada linha, o código imprime os números na sequência, aumentando num a cada iteração e garantindo que os números sejam alinhados corretamente.
- Mensagem de Erro: Caso o usuário insira um número menor ou igual a zero, uma mensagem de erro personalizada será exibida.
