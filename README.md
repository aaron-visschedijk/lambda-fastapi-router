# Router for running fastapi on Lambda

Running fastapi on lambda can cause some issues that will cause the router to get stuck in an infinite 307 redirect loop. This tiny wrapper for the fastapi APIRouter aims to solve this issue.


## Installation

```
pip install lambda-fastapi-router
```

## Usage

This router is used the same way as the fastapi APIRouter:

```python
from lambda_fastapi_router import LambdaRouter

router = LambdaRouter()

@router.get("/"):
async def root():
  return {"message": "Hello World!"}
```

Check the [fastapi docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=apirouter#another-module-with-apirouter) for more information.


## Why is this not part of FastAPI?

While this package solves the aforementioned issue, it is more of a workaround than a solution for the underlying issue. When adding a path on the LambdaRouter it really creates two paths on the underlying APIRouter, one with a trailing dash and one without. This solves the issue since a redirect is then necessary to access the resource. Ideally the bug is properly fixed in FastAPI such that it redirects correcly instead of creating double paths.
