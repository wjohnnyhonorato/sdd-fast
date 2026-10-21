"""Confere a estrutura de CURRENT_TASK.md ao abrir ou fechar uma tarefa."""

import argparse
import re
from pathlib import Path


HEADINGS = (
    "O que fazer",
    "O que não fazer",
    "Como validar",
    "Atritos no processo de implementação",
    "Checkpoint",
)
STATES = ("ainda não avaliado", "nenhum atrito observado", "atritos registrados")


def check_task(content: str, stage: str) -> list[str]:
    """Recebe o Markdown e a etapa; verifica seções e estado; devolve erros."""
    sections = list(re.finditer(r"^## (.+?)\s*$", content, re.MULTILINE))
    names = [match.group(1).strip() for match in sections]
    errors = [f"Seção obrigatória ausente: ## {name}" for name in HEADINGS if name not in names]
    errors += [f"Seção duplicada: ## {name}" for name in HEADINGS if names.count(name) > 1]

    if names.count("Atritos no processo de implementação") == 1:
        index = names.index("Atritos no processo de implementação")
        start = sections[index].end()
        end = sections[index + 1].start() if index + 1 < len(sections) else len(content)
        states = re.findall(r"^- Estado:\s*(.+?)\s*$", content[start:end], re.MULTILINE)
        if len(states) != 1:
            errors.append("Atritos: é necessário exatamente um '- Estado: ...'.")
        else:
            state = states[0].strip().removesuffix(".")
            if state not in STATES:
                errors.append("Atritos: estado desconhecido.")
            elif stage == "close" and state == "ainda não avaliado":
                errors.append("Atritos: avalie o estado antes de concluir ou arquivar.")
    return errors


def main() -> int:
    """Recebe etapa e caminho; imprime falhas estruturais; devolve código de saída."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("open", "close"))
    parser.add_argument("path", nargs="?", type=Path, default=Path("CURRENT_TASK.md"))
    args = parser.parse_args()
    try:
        content = args.path.read_text(encoding="utf-8")
    except OSError as exc:
        parser.exit(1, f"Não foi possível ler {args.path}: {exc}\n")
    errors = check_task(content, args.stage)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("Estrutura da tarefa: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
