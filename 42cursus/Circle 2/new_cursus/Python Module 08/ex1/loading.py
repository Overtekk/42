import importlib.util
from types import ModuleType


def check_dependency(module_name: str) -> ModuleType | None:

     name = importlib.util.find_spec(module_name)
     if name is None:
          return None

     module = importlib.import_module(module_name)
     return module


def main() -> None:

    print("\nLOADING STATUS: Loading programms..\n")

    print("Checking dependecies:")

    dependecies_list = ["pandas", "requests", "matplotlib"]
    dependecies_installed = []

    for object in dependecies_list:
        module = check_dependency(object)
        if module is None:
             print(f"ERROR: {object} is not installed. Please install it using"
                   " pip install -r requirements.txt) or Poetry "
                   "(poetry install).")
        else:
            dependecies_installed.append(module)

    if len(dependecies_installed) < 3:
        return

    for module in dependecies_list:
        name = __import__(module)
        version = name.__version__
        if module == "pandas":
            print(f"[OK] {module} ({version}) - Data manipulation ready")
        elif module == "requests":
            print(f"[OK] {module} ({version}) - Network access ready")
        elif module == "matplotlib":
            print(f"[OK] {module} ({version}) - Visualization ready")

    pandas = dependecies_installed[0]
    requests = dependecies_installed[1]

    print("\nSimulate request...")

    try:
        response = requests.get("https://www.python.org/")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(f"Status: {response.status_code}\n {response.headers}")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data = pandas.DataFrame([{'A': 1.1, 'B': 2, 'C': 3.3, 'D': 4},
                             {'A': 2.7, 'B': 10, 'C': 5.4, 'D': 7},
                             {'A': 5.3, 'B': 9, 'C': 1.5, 'D': 15}])
    print(data)

    print("\nGenerating visualization...")

    import matplotlib.pyplot as plt

    filename = "matrix_analysis.png"

    data.plot(kind='bar', title="Matrix Analysis Simulation")
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.savefig(filename)

    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


if __name__ == "__main__":
    main()
