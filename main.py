import importlib
import pkgutil

def load_classes_from_module(module):
    classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)
    return classes

# Load all modules from the AO3 package
ao3_package = importlib.import_module("AO3")
module_names = [
    name
    for _, name, _ in pkgutil.iter_modules(ao3_package.__path__)
    if name != "__init__"
]

# Import each module dynamically and get classes
all_classes = []
for module_name in module_names:
    module = importlib.import_module(f"AO3.{module_name}")
    module_classes = load_classes_from_module(module)
    all_classes.extend(module_classes)

# Now, you can use the classes as needed
for class_obj in all_classes:
    # Do something with each class, e.g., instantiate or use them
    instance = class_obj()
    # ...

# Access the FastAPI application instance
app = ao3_package.app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
