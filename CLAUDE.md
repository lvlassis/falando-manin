# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Verso** is a compiler/transpiler for **Romântica** ("Linguagem Poética"), a programming language where programs look like Portuguese Romantic-era poetry. The compiler targets C code output. This is a final project for a Formal Languages (Linguagens Formais) course at UFG.

See `docs/Linguagem Poética.md` for the full language spec and `docs/rascunho_objetivo_2.md` for syntax examples.

## Running

```bash
python main.py
```

Tests (currently stubs):

```bash
python tests/tokenization.py
```

## Architecture

The compiler pipeline lives in the `verso/` package:

- `verso/tokens.py` — defines the `Token` dataclass (`type`, `value`) and the `TOKEN_TYPES` list
- `verso/tokenization.py` — `tokenization(program) -> list[Token]` stub; the main entry point for lexing
- `main.py` — top-level entry point (empty)
- `tests/tokenization.py` — test file for the tokenizer (empty)

The compiler pipeline is: **source text → tokenization → (parsing → AST → C codegen, not yet implemented)**.

## Language Semantics

Romântica programs resemble Portuguese romantic poetry and transpile to C. Key constructs:

**Type keywords** (mapped to C types):
- `Rocha` → `int`
- `Bruma`, `Névoa`, `Cinza` → `float`
- `Traço`, `Suspiro` → `char`
- `Verso`, `Canção`, `Prosa` → `char[]` (string)
- `Dilema`, `Dualidade` → `bool`

**Declaration patterns:**
- `<var> é <type>.` → `type var;`
- `Que <var> seja <type>.` → `type var;`
- `Que <var> seja <type> <adjective>.` → `type var = value;`

**Assignment keywords:** `é`, `és`, `guarda`, `encerra`, `seja`, `guarde`, `encerre`

**Control flow:**
- `se … então` → `if`
- `porém, se|caso` → `else if`
- `senão` → `else`
- `enquanto` → `while`
- `para` → `for`
- `.` (period) → block terminator `}`

**Output:** `gritarei` / `digo que` → `print`

**Comments:** Lines starting with `#`

**Arrays:** `Coro`, `Compêndio` — declared with adjective denoting element type (e.g., `rochoso` for int array)

Numeric values are encoded as adjectives/descriptions rather than literals; length of a list of values determines array size. See `docs/Linguagem Poética.md` for the full grammar discussion.
