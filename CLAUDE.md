# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Verso** is a compiler/transpiler for **Romântica** ("Linguagem Poética"), a programming language where programs look like Portuguese Romantic-era poetry. The compiler targets C code output. Final project for a Formal Languages (Linguagens Formais) course at UFG.

Full language spec: `docs/Linguagem Poética.md`. Syntax examples: `docs/rascunho_objetivo_2.md`.

## Running

```bash
python main.py
```

## Architecture

All compiler logic lives in `verso/tokens.py`. The pipeline per line is:

1. `filter_comments(line)` — strips `#` comments
2. `verso_split(line)` — splits on spaces and isolates `.` as its own token
3. **Weak pass** (`tokenize_word_weak`) — classifies each word independently; unrecognized words become `TokenType.WEAK`
4. **Strong pass** (`tokenize_strong`) — reclassifies `WEAK` tokens using surrounding context (e.g. the word before `DECLARATION` becomes `VARIABLE`)

Each line ends with `TokenType.EOL` appended to the flat token list. The result is a `TokenList`.

### TokenList

`TokenList` wraps `list[Token]` and exposes:
- `find(tipo: TokenType)` — returns `(Token, index)` of the first match, or `None`
- `merge(start, end, token_type)` — replaces `tokens[start:end]` with a single token whose value is the joined string values of the slice

## Enums

**`TokenType`** — type of a token; add new members here when introducing new syntax:

| Member | Meaning |
|---|---|
| `WEAK` | Unclassified word (upgraded in strong pass) |
| `DOT` | `.` — statement/block terminator |
| `DECLARATION` | `é` / `és` — declaration or assignment keyword |
| `VARIABLE` | Identifier (reclassified from WEAK when before DECLARATION) |
| `PRIMITIVE_TYPE` | Type keyword; `value` holds a `PrimitiveType` member |
| `NUMERICAL_EXPRESSION` | Collapsed adjective phrase representing a numeric value |
| `EOL` | End of line sentinel |

**`PrimitiveType`** — value stored in a `PRIMITIVE_TYPE` token; add new members here when introducing new types:

| Member | Romântica keywords |
|---|---|
| `INTEGER` | `rocha` |
| `FLOAT` | `bruma`, `névoa`, `cinza` (not yet implemented) |

## Language Semantics

**Types** (keyword → C type):
- `Rocha` → `int`
- `Bruma`, `Névoa`, `Cinza` → `float`
- `Traço`, `Suspiro` → `char`
- `Verso`, `Canção`, `Prosa` → `char[]`
- `Dilema`, `Dualidade` → `bool`

**Declaration patterns:**
- `<var> é <type>.` → `type var;`
- `Que <var> seja <type>.` → `type var;`
- `Que <var> seja <type> <adjective>.` → `type var = value;`

**Assignment aliases for `é`:** `és`, `guarda`, `encerra`, `seja`, `guarde`, `encerre`

**Numeric values** are encoded as adjective phrases (not literals); the phrase between the type token and the next `.` or EOL becomes a `TOKEN_NUMERICAL_EXPRESSION`.

**Control flow:** `se … então` → `if` | `porém, se|caso` → `else if` | `senão` → `else` | `enquanto` → `while` | `para` → `for` | `.` → `}`

**Output:** `gritarei` / `digo que` → `print`

**Arrays:** `Coro`, `Compêndio` — element type indicated by adjective (e.g. `rochoso` for int)
