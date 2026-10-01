# Project Plan
---

### 1. Initial Structure

| Objective | Statut |
| :-------: | :----: |
| Create the github repo | ✅ |
| Create the Makefile | ✅ |

### 2. Rules

| Objective | Statut |
| :-------: | :----: |
| Using the model **Qwen/Qwen3-0.6B** | ✅ |
| Provide a CLI using Python Fire | ✅ |
| Implemente a progress bars using `tqdm` | ✅ |
| Repo contains: `src/`, `pyproject.toml`, `uv.lock`, `README.md` | ✅ |
| Flake8 norm | ❌ |
| Mypy norm | ❌ |
| Docstrings included in all functions and classes | ❌ |

### 3. RAG

#### 3.1 Knowledge Base Ingestion System

| Objective | Statut |
| :-------: | :----: |
| Give the LLM the VLLM repo (all files) | ✅ |
| Implement intelligent chunking for Python code and Markdown documentation | ✅ |
| Create a searchable knowledge index using `TF-IDF` or `BM25` | ✅ |
| Chunking Strategy for Python code chuncking | ✅ |
| Chunking Strategy for Text chunking | ✅ |
Configure maximum chunk size via CLI argument (maximum 2000 characters) | ✅ |
| Store the index for fast retrieval (max 5 minutes indexing time) | ✅ |

#### 3.2 Retrieval System

| Objective | Statut |
| :-------: | :----: |
| Implement semantic search over the indexed knowledge base | ✅ |
| Return top-k most relevant code snippets for any querry | ✅ |
| Each result must include: `file_path`, `first_character_index`, `last_character_index` | ✅ |
| Support batch processing of multiple questions from JSON datasets | ✅ |
| Achieve at least 80% recall@5 on docs questions and 50% on code questions | ✅ |

#### 3.3 Answer Generation System

| Objective | Statut |
| :-------: | :----: |
| Pass retrieved context to the LLM withing token limits | ✅ |
| Generate answers based on the retrieved code and documentation | ✅ |
| Output structured JSON following the provided pydantic models | ✅ |

##### Good Answer:

| Objective | Statut |
| :-------: | :----: |
| Readable without seeing the original question | ✅ |
| Cites the source(s) it draws from | ❌ |
| Limits itself to source content (no hallucination) | ✅ |
| Directly answers the queston asked | ✅ |

#### 3.4 Evaluation System

| Objective | Statut |
| :-------: | :----: |
| Implement recall@k metric to measure retrieval quality | ✅ |
| Compare retrieved sources against ground truth annotations | ✅ |
| Calculate overlap between retrieved and correct souces (minimum 5% overlap counts as found) | ✅ |
| Provide detailed performance metrics | ✅ |

#### 3.5 CLI

| Objective | Statut |
| :-------: | :----: |
| `index` (index the repository) implemented | ✅ |
| `search` (search for a single query) implemented | ✅ |
| `search_dataset` (process multiple questions and output search results) implemented | ✅ |
| `answer` (answer a single question with context) | ✅ |
| `answer_dataset` (generate answers from search results) | ✅ |
| `evaluate` (evaluate search results against ground truth) | ✅ |
| Handle edge cases and degenerate inputs gracefully with clear error messages | ✅ |

### 4. Data Models

| Objective | Statut |
| :-------: | :----: |
| Implement `MinimalSource` model (`file_path`, `first_character_index`, `last_character_index`) | ✅ |
| Implement `UnansweredQuestion` and `AnsweredQuestion` models | ✅ |
| Implement `RagDataset` model | ✅ |
| Implement `MinimalSearchResults` and `MinimalAnswer` models | ✅ |
| Implement `StudentSearchResults` and `StudentSearchResultsAndAnswer` models | ✅ |

### 5. Output

| Objective | Statut |
| :-------: | :----: |
| Search operations: `StudentSearchResults` models with `search_results` and `k` | ✅ |
| Answer generation: `StudentSearchResultsAndAnswer` model with `search_results` and `k` | ✅ |
| Source information: `MinimalSource` contains `file_path`, `first_character_index`, `last_character_index` | ✅ |
| Output strictly formatted as a comprehensive JSON file respecting the Pydantic models | | ✅ |

### 6. Evaluation

| Objective | Statut |
| :-------: | :----: |
| Performance indexing time: 5 minutes max | ✅ |
| Performance cold start latency: 60 seconds max | ✅ |
| Performance warm retrieval throughput: 90 seconds maximum for 1000 questions | ✅ |
| Performance recall@5: 80% on docs questions, 50% on code | ✅ |

### 7. Bonus

| Objective | Statut |
| :-------: | :----: |
| Query expansion (e.g. synonym expansion, query rewriting) | ❌ |
| Semantic embeddings for retrieval | ❌ |
| Result caching (index caching, query caching, etc.) | ❌ |
| Hybrid retrieval combining multiple methods | ❌ |
| Local LLM inference via VLLM | ❌ |

### 8. README

| Objective | Statut |
| :-------: | :----: |
| Global structure of the README | ❌ |
| Initial texts | ❌ |
| Additionals Sections | ❌ |
