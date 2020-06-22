import os

from invoke import task

REPO_DIR = os.path.dirname(__file__)


@task
def update_adr(c, render_puml=True):
    if render_puml:
        c.run(f"plantuml -v {REPO_DIR}/doc/adr/")
    c.run(f"adr generate toc -o {REPO_DIR}/doc/adr/.outro.md > {REPO_DIR}/doc/adr/README.md")
