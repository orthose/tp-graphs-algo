import inspect
from typing import Callable
from pygments import highlight                   # type: ignore
from pygments.lexers import PythonLexer          # type: ignore
from pygments.formatters import HtmlFormatter    # type: ignore
from IPython.display import display, HTML        # type: ignore


def show_source(function: Callable) -> None:
    code = inspect.getsource(function)
    lexer = PythonLexer()
    formatter = HtmlFormatter(cssclass='pygments')
    html_code = highlight(code, lexer, formatter)
    css = formatter.get_style_defs('.pygments')
    html = f"<style>{css}</style>{html_code}"
    display(HTML(html))


def code_checker(command: str) -> None:
    import subprocess

    result = subprocess.run(command.split(), capture_output=True)
    print(result.stdout.decode())
    if result.returncode:
        raise RuntimeError(
            f"La commande {command} a émis des avertissements:\n\n"
        )
