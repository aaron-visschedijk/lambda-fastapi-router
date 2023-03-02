# Router for running fastapi on Lambda

Running fastapi on lambda can cause some issues that will cause the router to get stuck in an infinite 307 redirect loop. This tiny wrapper for the fastapi APIRouter aims to solve this issue.


# Installation

```
pip install lambda-fastapi-router
```

# Usage

This router is used the same way as the fastapi APIRouter:

```python
from lambda_fastapi_router import LambdaRouter

router = LambdaRouter()

@router.get("/"):
async def root():
  return {"message": "Hello World!"}
```

Check the [fastapi docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=apirouter#another-module-with-apirouter) for more information.
