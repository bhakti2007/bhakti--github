import os
from git import Repo

repo = Repo.init(os.getcwd())
repo.git.checkout("-b", "add-code-files")
repo.index.add(["file1.py", "file2.py"])
repo.index.commit("Add initial code files")

origin = repo.create_remote(
    "origin",
    f"https://{os.getenv('GITHUB_USER')}:{os.getenv('GITHUB_PAT')}@github.com/{os.getenv('GITHUB_USER')}/{os.getenv('REPO')}.git"
)
origin.push(refspec="add-code-files:add-code-files")