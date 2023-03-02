# Router for running fastapi on Lambda

Running fastapi on lambda can cause some issues that will cause the router to get stuck in an infinite 307 redirect loop. This tiny wrapper for the fastapi APIRouter aims to solve this issue.


# Usage

This router is used the same way as the fastapi APIRouter
