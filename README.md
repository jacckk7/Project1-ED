# Project1-ED
Primeiro projeto da disciplina de Estrutura de Dados
Instruções do Projeto 1:

A nova nave do império, a temida BAT2, está quase pronta para aniquilar a ameaça rebelde. Falta apenas o núcleo de controle de processos concorrentes para que ela funcione a plena capacidade. O sistema operacional se encarrega de enviar as solicitações de processos, e você foi designado para implementar o controle da ordem de execução de partes dos processos utilizando a abordagem round-robin. O sistema operacional já determina a fatia de tempo de cada solicitação: a execução de um comando especial.

Basta implementar as seguintes funcionalidades:

-> add X adiciona uma solicitação com X>0 processos à fila de execução. Este comando é seguido de X instâncias de um dos 3 comandos especiais listados a seguir, que devem ser executados na ordem em que são fornecidos para completar o processo.
  - crypto S define a chave criptográfica para envio de mensagens aos heróis do Império, visando garantir sua segurança ante espiões rebeldes. A partir da sequência S de não mais que 8 símbolos + ou − que indicam, respectivamente, que a ordem dos dígitos adjacentes deve ser crescente ou decrescente. Este comando gera o menor número possível com dígitos distintos.
  - deYodafy W decodifica as instruções do Mestre Yoda, fornecidas como uma sequência W de palavras (e pontuação), invertendo sua ordem para que façam sentido e, portanto, sirvam para as decisões táticas da BAT2.
  - merge I facilita a perseguição aos rebeldes simplificando o espaço de busca: apresenta uma sequência de intervalos sem sobreposição, em ordem, criada a partir dos I intervalos dados (que indicam as coordenadas onde se sabe que a paz do Império reina absoluta). Cada intervalo é definido por valores inteiros no formato [x,y], separados por espaço, tais que x≤y (há um espaço após a vírgula entre x e y).

-> halt interrompe a execução e mostra quantas solicitações ficaram órfãs (não foram finalizadas) e a quantidade total de comandos que não foram executados.

-> process executa o próximo comando especial disponível conforme o algoritmo round-robin.

A comunicação com o sistema é simples, as funcionalidades são apresentadas como descritas acima pelo sistema operacional, e seu programa deve organizá-las e executá-las conforme solicitado pelas instâncias superiores.
