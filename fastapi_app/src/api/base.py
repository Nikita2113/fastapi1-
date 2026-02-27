from fastapi import APIRouter, status, HTTPException

from schemas.posts import Post, PostBase


router = APIRouter()


@router.get("/hello_world", status_code=status.HTTP_200_OK)
async def get_hello_world() -> dict:
    response = {"text": "Hello, World!"}

    return response


@router.post("/test_json", status_code=status.HTTP_201_CREATED, response_model=Post)
async def test_json(post: Post) -> dict:
    if len(post.text) < 3:
        raise HTTPException(
            detail="Длина поста должна быть не меньше 3 символов",
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )

    response = {
  "id": 0,
  "author": {
    "login": "string",
    "id": 0,
    "created_at": "2026-02-27T14:28:49.181Z"
  },
  "category": {
    "id": 0,
    "author": {
      "login": "string",
      "id": 0,
      "created_at": "2026-02-27T14:28:49.181Z"
    },
    "title": "string",
    "description": "string",
    "is_published": 'true'
  },
  "text": "string",
  "datetime_to_publish": "2026-02-27T14:28:49.181Z",
  "created_at": "2026-02-27T14:28:49.181Z"
}

    return Post.model_validate(obj=response)