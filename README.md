# CLI Task Manager

A lightweight command-line task manager for organizing work, tracking progress, and keeping your to-do list in one place.

## Features

- Add new tasks
- List all tasks
- Mark tasks as complete or incomplete
- Delete tasks
- View pending tasks only
- Persist data locally between runs

## Requirements

- Python 3.9 or later

## Installation

Clone the project and move into the project directory:

```bash
git clone <repository-url>
cd CLI-TaskManager
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies if the project includes any:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, you can proceed directly to running the app.

## Usage

Run the application with:

```bash
python main.py
```

Common commands may look like:

```bash
python main.py add "Write project README"
python main.py list
python main.py done 1
python main.py delete 2
python main.py pending
```

If your project uses a different entry point, replace `main.py` with the actual file name.

## Example Workflow

```bash
python main.py add "Plan sprint tasks"
python main.py add "Fix CLI bug"
python main.py list
python main.py done 1
python main.py pending
```

## Project Structure

A typical structure for this project might look like:

```text
CLI-TaskManager/
├── main.py
├── task_manager.py
├── tasks.json
├── README.md
├── requirements.txt
└── .gitignore
```

If your repository differs slightly, keep the same basic structure and adapt the file names accordingly.

## Data Storage

Tasks are typically stored in a local JSON file such as `tasks.json` so your task list remains available between sessions.

## Notes

This project is designed to be simple and easy to use from the terminal. It is suitable for personal productivity tracking and small project management workflows.

## Contributing

Contributions are welcome. If you want to improve the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project does not include a license file yet. If you want to publish it publicly, consider adding an open-source license such as MIT.

If you want, I can also generate a version tailored to the exact files in your project once you share the folder structure or key source files.
