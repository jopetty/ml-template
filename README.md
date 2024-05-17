# ml-research-kit

A template for developing an ML experimentation framework.

## Local Installation

All python dependencies are provided in `pyproject.toml`. Install using `uv`:

1. `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. `uv venv`
3. `source .venv/bin/activate`
4. `uv pip install -e .`

To generate a set of locked dependencies, run

```bash
uv pip compile pyproject.toml -o requirements.txt
```


## Docker / Devcontainer

There's a built-in Dockerfile and devcontainer configuration to make running
the project in a remote container from VSCode easy. Just install the remote containers
extension and open the project in a container.
