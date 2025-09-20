import os
import git
from langchain_community.document_loaders import (
    DirectoryLoader, 
    TextLoader, 
    PythonLoader, 
    NotebookLoader
)

def load_github_repo(
    repo_url: str, 
    repo_path: str = None, 
    file_types: dict = None
) -> list:
    """
    Clone or update a GitHub repository locally, then load source code and documentation files
    into LangChain Document objects.

    Args:
        repo_url (str): The GitHub repository URL.
        repo_path (str): Local path to store the repo.
        file_types (dict): Mapping of file extensions to loader classes.
                           Example: {".py": PythonLoader, ".md": TextLoader}

    Returns:
        List[Document]: A list of LangChain Document objects containing code & docs.
    """

    # Clone or pull the repo
    # If repo_path not provided, derive from repo name
    if repo_path is None:
        repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
        repo_path = f"./{repo_name}"
    if not os.path.exists(repo_path):
        print(f"Cloning repository from {repo_url} ...")
        git.Repo.clone_from(repo_url, repo_path)
    else:
        print(f"Repository already exists at {repo_path}. Pulling latest changes...")
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.pull()

    # Default file types if not provided
    if file_types is None:
        file_types = {
            ".py": PythonLoader,
            ".ipynb": NotebookLoader,
            ".md": TextLoader,
            ".txt": TextLoader,
            ".rst": TextLoader,
            ".json": TextLoader,
            ".yaml": TextLoader,
            ".yml": TextLoader,
            ".toml": TextLoader,
            ".ini": TextLoader,
            ".cfg": TextLoader,
            ".csv": TextLoader,
            ".tsv": TextLoader,
            ".html": TextLoader,
            ".css": TextLoader,
            ".js": TextLoader,
            ".java": TextLoader,
            ".cpp": TextLoader,
            ".c": TextLoader,
            ".h": TextLoader,
            ".go": TextLoader,
            ".rs": TextLoader,
            ".php": TextLoader,
            ".rb": TextLoader,
            ".swift": TextLoader,
            ".kt": TextLoader,   # Kotlin
            ".scala": TextLoader,
            ".sh": TextLoader,
            ".bat": TextLoader,
            ".ps1": TextLoader,
            ".dockerfile": TextLoader,
            "Dockerfile": TextLoader,  # special case (no extension)
        }

    # Build loaders dynamically
    all_docs = []
    for ext, loader_cls in file_types.items():
        pattern = f"**/*{ext}" if not ext.lower().startswith("dockerfile") else "**/Dockerfile"
        loader = DirectoryLoader(repo_path, glob=pattern, loader_cls=loader_cls, show_progress=True)
        docs = loader.load()
        all_docs.extend(docs)

    print(f"Loaded {len(all_docs)} documents from {repo_url}")
    return all_docs