---
thumbnail: tree_abiss.png
---
#homepage

See also: [[Homepage]]
- - - 

## Tipos Primitivos

*OBS:* Para detalhes relativos à declaração/atribuição, veja o capítulo [[Linguagem Poética#Declaração e atribuição|Declaração e atribuição]].

* **int**: *Rocha* (Esta foi minha última adição, e eu já estava sem criatividade)

```bash 
Amor é Rocha. # int amor;
Este encerra o dom de viver e de odiar. # amor = 1325125

Que a ira seja rocha que te afunde em água pútrida. # int amor = 326257
```
*OBS:* Para detalhes sobre a keyword `encerra` (contém), vide [[Linguagem Poética#Declaração e atribuição|Declaração e atribuição]].
*OBS:* Para detalhes sobre a keyword `Este`, vide [[Pronomes]].

* **float**: *Bruma*/*Névoa* (Sem limite definido, é algo esparso, não inteiro), *Cinza* (Partes restantes de algo que já foi inteiro)

```bash 
Paixão é bruma que se esvai... poeira que se leva. # float Paixão = 325.6324
Que a morte seja cinza de minha vida queimada... # float morte = 2548.0
```

* **fixed**: *Ainda estou na dúvida do que se trata*

* **char**: *Traço*, *Suspiro* (Algo curto, breve, contido como um char...?...)

*OBS: Pega a primeira letra após declaração*
```bash 
A vida é um suspiro breve; #char vida = 'b'
Que a vida seja traço suave em páginas divinas. # char vida = 's' 
```

* **string**: *Verso*, *Canção*, *Prosa* (Sem necessidade de explicações)

```bash 
Que o amor seja um verso. # char amor[]; // Em 'c' isto inválido

A saudade é uma canção amarga. # char saudade[6]; // Em 'c' isto é correto 

Que a vida seja como a poesia: "Batatinha quando nasce...". 
# char vida[] = "Batatinha quando nasce..." 
```

* **bool**: *Dilema*, *Dualidade* (Sem necessidade de explicações)

```bash 
Viver é um verdadeiro dilema. # int viver = 1 // Já que 'C' não tem bool
```
*OBS:* Podemos criar uma lista de apelidos para true e false que se encaixe na poesia, como *glórias, vitórias, conquistas,* (*true*) e *enfados, derrotas, tristezas* (*false*) e seus respectivos adjetivos.
## Estruturas de dados

Para determinar o tipo dos dados a serem armazenados na estrutura de dados, adjetivos relacionados ao dado serão utilizados:

Ex: *rochoso* (inteiro), *dual* (booleano), *enevoado* (float), *prosaico* (string)

* **Arrays**: *Coro*, *Compêndio*

```bash 
A história é um compêndio dual velho que encerra glórias, vitórias, conquistas, derrotas e tristezas. # # int (bool) história[5] = [1, 1, 1, 0, 0];
```
*OBS:* Veja a explicação no exemplo de atribuição de arrays em [[Linguagem Poética#Declaração e atribuição|Declaração e atribuição]].

* **Matrizes**
* **Multidimensionais**
## Estruturas chave-valor

* **Dicionários**
* **Hash-Tables**
* **Maps**

## Estruturas personalizadas

* **Structs**
## Declaração e atribuição

### Declaração e inicialização

* **\<?artigo\> \<var\> é \<?artigo\> \<tipo\>**

**Ex:** O prazer é névoa. *#float prazer;*

*Apelidos válidos para 'é':* és

* **Que \<?artigo\> \<var\> seja \<?artigo\> \<tipo> \<?Valor>**

**Ex:** Que o amor seja rocha. *# int amor;*
**Ex:** Que o amor seja rocha inabalável. *# int amor = 10*

#### Arrays

* **\<?artigo\> \<var\> é \<?artigo\> \<array_keyword\> \<tipo\> \<size\>**

**Ex:** A história é um compêndio dual velho. *# int (bool) historia[5];*

* **\<?artigo\> \<var\> é \<?artigo\> \<array_keyword\> \<tipo_adj\> \<?size\> que \<attribution_keyword\> \<values\>**

**Ex:** A história é um compêndio dual que encerra glórias, vitórias, conquistas, derrotas e tristezas. *# int (bool) história[] = [1, 1, 1, 0, 0];*
### Atribuição

* **\<?artigo\> \<var\> é \<?artigo\> \<valor\>**

**Ex:** O prazer é passageiro... o amor é eterno. *# prazer = 10.1416;*

*Apelidos válidos para 'é' na ATRIBUIÇÃO:* és, guarda, encerra.

**Ex:** Tu és valioso. *# tu = 7*
**Ex:** O coração guarda mágoas. *# coracao = 6*
**Ex:** O coração encerra mágoas. *coracao = 6*

* **Que \<?artigo\> \<var\> seja \<?artigo\> \<valor>**

**Ex:** Que a amizade seja regente e nossas vidas orquestra. *amizade = 71659*

*Apelidos válidos para 'seja' na ATRIBUIÇÃO:* guarde, encerre.

**Ex:** Que a morte guarde as mágoas que sobraram. *# morte = 2638*
**Ex:** Que a vida encerre em seu ceio a alegria. *# vida = 823417*
#### Arrays

A pensar...

## Pronomes

Recurso disponível na linguagem *Rockstar*.

Não tenho certeza se vai dar tempo de colocar. Provavelmente não. Mas segue um exemplo da ideia.

```bash 
Amor é Rocha. # int amor;
Este encerra o dom de viver e de odiar. # amor = 1325124
```
