from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import time
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from .routers import post, user, auth, vote
from pydantic_settings import BaseSettings
from .config import settings




# models.Base.metadata.create_all(bind=engine)



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

get_db()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='1313', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was succesfull')
#         break
#     except Exception as error:
#         print('Connecting to database failed')
#         print(f'Error: {error}')
#         time.sleep(2)


# my_posts = [{'title': 'title of post1', 'content': 'content of post 1', 'id': 1}, 
#             {'title': 'title of xd', 'content': 'content of post xd', 'id': 2}]



# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i






# @app.get("/")
# def root():
#     return {"message": "welcome"}



# @app.get('/posts', response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db)):
#     # cursor.execute("""SELECT * FROM posts """)
#     # posts = cursor.fetchall()
#     posts = db.query(models.Post).all()
#     return posts



# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # post_dict = post.dict()
#     # post_dict['id'] = randrange(0, 10000)
#     # my_posts.append(post_dict)
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
#     # new_post = cursor.fetchone()
#     # conn.commit()

#     # new_post = models.Post(title=post.title, content=post.content, published = post.published)
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @app.get('/posts/{id}', response_model=schemas.Post)
# def get_post(id: str, db: Session = Depends(get_db)):
#     # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
#     # post = cursor.fetchone()
#     # post = find_post(int(id))
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'message': f'post with id: {id} was not found'}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} was not found')
#     return post


# @app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):

#     # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
#     # deleted_post = cursor.fetchone()
#     # conn.commit()
#     # index = find_index_post(id)
#     post = db.query(models.Post).filter(models.Post.id == id)

#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exist')
#     # my_posts.pop(index)
#     post.delete(synchronize_session=False)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):

#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
#     # updated_post = cursor.fetchone()

#     # index = find_index_post(id)
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exist')
#     post_query.update(updated_post.dict(), synchronize_session=False)
#     db.commit()
#     # post_dict = post.dict()
#     # post_dict['id'] = id
#     # my_posts[index] = post_dict
#     return post_query.first()




# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     #hash the password - user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password

#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/users/{id}', response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first() 
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {id} does not exist')
#     return user