###
Terminal cd s05_langchain
conda create -p venv python==3.13.9

A) On terminal:
    1) conda activate ./venv
    2) conda activate ./venv
    3) python -m ipykernel install --user --name=venv --display-name "s05_langchain:Python (venv)"
B) Switch the kernel in VS code to "s04_pydantic:Python (venv)"
C) In notebook run below:
    1) import sys
    2) print(sys.executable) --> should print .../s04_pydantic/venv/...
    3) !pip install pydantic
    4) Now importing pydantic should not give error