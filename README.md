# ProgramacaoDeComputadores

Alunos: Jonathan Alves

Curso: ADS
___________________________________________________________________________________________________________________________________________________________________________________________
# **Estruturas de Controle do Fluxo de Execução**

São construções na programação que possibilitam determinar a ordem em que os comandos de um programa são executados, dependendo das instruções presentes. Essas estruturas podem ser divididas em:

Estruturas sequenciais
Estruturas condicionais (de decisão)
Estruturas de repetição (laços)

# **Seção 01 - Estrutura Sequencial**

Nesse tipo de estrutura, as instruções de um algoritmo ou programa são executadas numa ordem fixa e pré-definida. Cada comando só começa a ser processado após o término do comando anterior, seguindo uma sequência linear de cima para baixo, respeitando a ordem em que foram escritas.

Exemplo em sequencial.py

# **Seção 02 - Estruturas Condicionais**

Nas estruturas condicionais, o computador apresenta um comportamento mais "inteligente" — sem confundir com inteligência artificial — pois passa a decidir quais ações executar com base em uma condição lógica, que é uma expressão que resulta em verdadeiro ou falso. Dessa forma, o fluxo do programa pode mudar dependendo do resultado da avaliação dessas condições.

Essas condições avaliam estados de variáveis ou expressões, retornando sempre um valor booleano: verdadeiro (V) ou falso (F).
As estruturas condicionais são classificadas conforme a quantidade de condições a serem avaliadas, podendo ser:
Estruturas do tipo "Se"
Estruturas do tipo "Escolha"
Estruturas Condicionais do tipo "Se"
Neste formato, uma única condição lógica é avaliada. Caso essa condição seja verdadeira, um comando simples ou um bloco de comandos é executado; caso seja falsa, outro comando ou conjunto diferente pode ser executado. Se não houver comandos para o caso falso, a execução segue normalmente sem realizar nenhuma ação.

Exemplo em decisao_idade.py

# **Seção 03 - Estruturas de Repetição**

Também conhecidas como laços ou loops, essas estruturas têm o objetivo de repetir partes específicas do programa várias vezes.

Repetir blocos de código é uma prática comum e útil na programação, pois facilita a reutilização de instruções. Por exemplo, ao fazer cálculos financeiros onde a fórmula é a mesma, mas os valores mudam conforme o tempo.
As estruturas de repetição estão ligadas às estruturas de decisão, pois o controle do início, continuação ou término do laço depende da avaliação de condições lógicas.
Os laços podem ser classificados conforme o conhecimento prévio ou não da quantidade de repetições:
Laços contados — quando se sabe de antemão quantas vezes o bloco de comandos será executado.
Laços condicionais — quando o número de repetições depende de uma condição que pode mudar dentro do próprio laço.
Laços Contados
São aqueles onde existe um mecanismo para contar o número de vezes que o corpo do laço deve ser executado. Também são chamados de laços do tipo "Para" ou "For".

Exemplo em repeticao_for.py

# **Construção Enquanto (While)**

Essa estrutura realiza a verificação da condição lógica no início do laço, testando se o bloco de comandos deve ser executado ou não. Para funcionar corretamente, é necessário que as variáveis envolvidas já estejam inicializadas antes da execução do laço.
Se a condição inicial for falsa, o bloco de comandos não será executado e o programa continuará normalmente a partir da instrução seguinte ao laço.
Se a condição for verdadeira, o bloco será executado e, ao final, a condição será testada novamente, repetindo esse processo enquanto a condição permanecer verdadeira. Quando a condição se tornar falsa, o laço termina e a execução do programa continua normalmente.
É fundamental garantir que em algum momento a condição avaliada se torne falsa; caso contrário, o laço pode se tornar infinito, travando a execução do programa.

Exemplo em repeticao_while.py

# Material de apoio teórico para esta aula se encontra nas seguintes seções do livro "Algoritmos e Programação I EBOOK.pdf":

ESTRUTURAS DE CONTROLE DO FLUXO DE EXECUÇÃO (página 103)

SEÇÃO 1- ESTRUTURA SEQUENCIAL (página 104)

SEÇÃO 2- ESTRUTURAS DE DECISÃO (página 114)

SEÇÃO 3- ESTRUTURAS DE REPETIÇÃO (página 135)
