# MCQGenerator - AI Coding Instructions

## Project Overview
MCQGenerator is a Python package that generates Multiple Choice Questions from text content using LLMs via LangChain. It integrates Hugging Face models, PDF processing, and Streamlit for UI.

**Stack:**
- **LLM Framework:** LangChain + Hugging Face Hub
- **UI:** Streamlit
- **Document Processing:** PyPDF2
- **Package Manager:** pip with setuptools

## Architecture

### Core Structure
```
src/mcqgenerator/     → Main package (currently minimal __init__.py)
experiment/mcq.ipynb  → Development/testing notebook
setup.py              → Package configuration
requirements.txt      → Dependencies (with editable install: -e .)
```

### Key Dependencies & Their Roles
- **langchain** + **langchain-community** + **langchain-huggingface:** LLM integration, prompt chaining, document processing
- **huggingface-hub:** Direct model access and authentication
- **pypdf2:** Extract text from PDF inputs
- **streamlit:** Web UI for the generator
- **python-dotenv:** Environment variable management (API keys, model selection)

## Development Workflow

### Initial Setup
```bash
pip install -r requirements.txt  # Installs dependencies + package in editable mode (-e .)
```
The `-e .` installs the package locally for development so changes to `src/mcqgenerator/` are immediately reflected.

### Development Pattern
1. **Experimentation:** Use `experiment/mcq.ipynb` for prototyping and testing LLM chains
2. **Implementation:** Move validated logic to `src/mcqgenerator/` modules
3. **Testing:** Verify in notebook before shipping

### Running the App
When Streamlit UI is implemented:
```bash
streamlit run app.py  # Or equivalent entry point
```

## Code Patterns & Conventions

### LangChain Integration
When implementing MCQ generation logic:
- Use LangChain's prompt templates for consistent prompt engineering
- Chain operations via LangChain's sequential/branching chains
- Load Hugging Face models via `langchain-huggingface` (not direct `transformers`)

### PDF Processing
- Use PyPDF2 to extract text from student-provided PDFs
- Clean extracted text before passing to LLM (remove headers, footers, extra whitespace)

### Environment Configuration
- Store sensitive data (HF tokens, API keys) in `.env` file
- Load via `python-dotenv`: `load_dotenv()` then `os.getenv("KEY")`
- Never commit `.env` to repository

### Error Handling
- Wrap LLM calls in try-except (notebook shows `traceback` imports for debugging)
- Handle API rate limits and token limits from Hugging Face models
- Validate PDF input and text extraction before LLM processing

## Integration Points

### External Dependencies
1. **Hugging Face Models:** Accessed via `langchain-huggingface` (e.g., `HuggingFaceHub`, `HuggingFaceInference`)
2. **LangChain Chains:** Compose prompts → LLM → parsing → validation
3. **Streamlit Components:** Input (file upload, text area), output (question display, JSON export)

### Data Flow
1. User provides text/PDF via Streamlit
2. PDF → Text extraction (PyPDF2)
3. Text → LangChain prompt engineering
4. LLM generates MCQs (Hugging Face model via langchain)
5. Parse LLM output to structured JSON/DataFrame
6. Display & export results via Streamlit

## Key Files to Understand
- [setup.py](setup.py) — Package metadata and dependency declaration
- [requirements.txt](requirements.txt) — Install-time dependencies
- [experiment/mcq.ipynb](experiment/mcq.ipynb) — Current development notebook

## Notes for AI Agents
- **Package is in early stage:** `src/mcqgenerator/` is minimal; most logic lives in notebook
- **No existing tests:** Add pytest tests in `tests/` as you implement features
- **Module structure TBD:** Plan modular design (e.g., `pdf_processor.py`, `mcq_generator.py`, `prompt_templates.py`)
- **Streamlit app missing:** Main UI entry point not yet created
