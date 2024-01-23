# api-test

# Setup local python dev environment


### Go to project root directory
`cd <project-dir>`

### Build image
`docker buildx build -t zfastapi .`

### Run app in container
`docker run --rm  -p 8000:8000 -v $(pwd)/src/app:/app --name devcontainer zfastapi:latest`

## Unit test
GitHub Copilot: To set up a development container in Visual Studio Code, you can use the **Codespaces: Add Dev Container Configuration Files...** command. This command will add the necessary configuration files to your workspace for setting up a development container.



japuvz: @workspace create a pydantic schema for items

GitHub Copilot: You can create a Pydantic schema for items in your [`app/main.py`](command:_github.copilot.openRelativePath?%5B%22app%2Fmain.py%22%5D "app/main.py") file. Here's an example of how you might define an [`Item`](command:_github.copilot.openSymbolInFile?%5B%22app%2Fmain.py%22%2C%22Item%22%5D "app/main.py") schema:

```python
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = None
```

In this schema, `id`, [`name`](command:_github.copilot.openSymbolInFile?%5B%22app%2Fmain.py%22%2C%22name%22%5D "app/main.py"), and [`price`](command:_github.copilot.openSymbolInFile?%5B%22app%2Fmain.py%22%2C%22price%22%5D "app/main.py") are required fields, while `description` and [`is_offer`](command:_github.copilot.openSymbolInFile?%5B%22app%2Fmain.py%22%2C%22is_offer%22%5D "app/main.py") are optional. Adjust the fields and types as necessary to fit your application's requirements.

japuvz: @Workspace create unit test for read_root

GitHub Copilot: You can create a unit test for the `read_root` function using the `FastAPI` test client. Here's an example of how you might do this in a new file `test_main.py`:

```python
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World1"}
```

This test uses the `TestClient` to send a GET request to the root endpoint, then checks that the response status code is 200 (indicating success) and that the JSON response matches the expected value.

japuvz: How can I run the unit tests for my FastAPI application in Visual Studio Code?

GitHub Copilot: To run unit tests for your FastAPI application in Visual Studio Code, you can use the built-in Python Test Explorer. Here are the steps:

1. Install the Python extension for Visual Studio Code if you haven't already. You can do this by searching for "Python" in the Extensions view (`Ctrl+Shift+X`).

2. Open the Command Palette (`Ctrl+Shift+P`) and run the "Python: Configure Tests" command.

3. In the dropdown that appears, select "pytest" as your test framework.

4. Select the directory where your test files are located. In your case, if your test file is in the root directory, just select the root directory.

5. After configuring, you should see a testing panel appear on the side bar where you can run and manage your tests. If you don't see it, you can open it by clicking on the beaker icon on the side bar, or by using the "Python: Show Test Output" command.

6. In the testing panel, you can run all tests by clicking on the "Run All Tests" button at the top. You can also run individual tests or test files by clicking on the "Run Test" button next to them.

Remember to install `pytest` in your project environment if you haven't already. You can do this by running `pip install pytest` in your terminal.