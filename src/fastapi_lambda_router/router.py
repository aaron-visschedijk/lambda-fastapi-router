from fastapi import APIRouter

class LambdaRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    
    def add_api_route(self, path, *args, **kwargs):
        super().add_api_route(path, *args, **kwargs)
        kwargs['include_in_schema'] = False
        if path == "":
            super().add_api_route("/", *args, **kwargs)
        elif path == "/":
            super().add_api_route("", *args, **kwargs)

