#Here is a basic implementation of a Personal Portfolio API using FastAPI and SQLite:

#API Endpoints

# PROJECTS

#POST /projects: Add a new project
-Request body: {"title": str, "description": str, "url": str}
-Response: {"id": int, "title": str, "description": str, "url": str}

#GET /projects: Get all projects
-Response: [{"id": int, "title": str, "description": str, "url": str}, ...]

#GET /projects/{project_id}: Get a single project
-Response: {"id": int, "title": str, "description": str, "url": str}

#PUT /projects/{project_id}: Edit a project
-Request body: {"title": str, "description": str, "url": str}
-Response: {"id": int, "title": str, "description": str, "url": str}

#DELETE /projects/{project_id}: Delete a project
-Response: {"message": "Project deleted successfully"}

# BLOG POSTS

#POST /blog-posts: Add a new blog post
-Request body: {"title": str, "content": str, "date": str,}
-Response: {"id": int, "title": str "content": str, "date": str}

#GET /blog posts: Get all blog posts
-Response: [{"id": int, "title": str, "content": str, "date": str}, ...]

#GET /projects/{blog-posts/{blog_post__id}: Get a single blog post
-Response: {"id": int, "title": str, "content": str, "date": str}

#PUT /blog-posts/{blog_post_id}: Edit a blog post
-Request body: {"title": str, "content": str, "date": str}
-Response: {"id": int, "title": str, "content": str, "date": str}

#DELETE /blog-posts/{blog_post_id}: Delete a blog post
-Response: {"message": "Blog post deleted successfully"}

# CONTACT INFORMATION 

#POST /contact-info: Add or edit contact information
-Request body: {"email": str, "phone": str, "address": str,}
-Response: {"email": str, "phone": str "address": str}

#GET /contact-info: Get contact information
-Response: {"email": str, "phone": str "address": str}

#DELETE /contact-info: Delete contact information
-Response: {"message": "Contact information deleted successfully"}


#FastAPI Code:

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

#Database connection
conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

#Models 
class Project(BaseModel):
    title: str
    description: str
    url: str

class BlogPost(BaseModel):
    title: str
    content: str 
    date: str

class ContactInfo(BaseModel):
    email: str 
    phone: str
    address: str

# Endpoints

@app.post("/projects")
def add_project(project:Project):
    cursor.execute("INSERT INTO projects VALUES(NULL, ?,?,?)", (project.title, project.description, project.url))
    conn.commit()
    return {"id": cursor.lastrowid, "title": project.title, "description": project.description, "url": project.url}

@app.get("/projects")
def get_projects():
    cursor.execute("SELECT*FROM projects")
    return cursor.fetchall()

@app.get("/projects/{project_id}")
def get_project(project_id:int):
    cursor.execute("SELECT*FROM projects WHERE id = ?", (project_id,))
    return cursor.fetchone()

@app.put("/projects/{projects_id}")
def edit_project(project_id: int, project:Project):
    cursor.execute("UPDATE projects SET title = ?, description = ?, url =? WHERE id = ?",(project.title, project.description, project.url, project_id))
    conn.commit()
    return {"id": project_id, "title": project.title, "description": project.description, "url": project.url}

@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    cursor.execute("DELETE FROM projects WHERE id = ?",(project_id,))
    conn.commit()
    return{"message": "Project deleted successfully"}

@app.post("/blog-posts")
def add_blog_post(blog:BlogPost):
    cursor.execute("INSERT INTO blogs VALUES(NULL, ?,?,?,)", (blog.title, blog.content, blog.date))
    return{"id": int, "title": blog.title, "content": blog.content, "date": blog.date}

@app.get("/blog-posts")
def get_blog_posts():
    cursor.execute("SELECT*FROM blog-posts")
    return cursor.fetchall()

@app.get("/blog-posts/{blog_post_id}")
def get_blog_post (blog_post_id:int):
    cursor.execute("SELECT*FROM blog-posts WHERE id = ?," (blog_post_id,))
    return cursor.fecthone()

@app.put("/blog-posts/{blog_post_id}")
def edit_blog_post (blog_post_id: int):
    cursor.execute ("UPDATE blog-posts SET title =?, content = ?, date = ? WHERE id = ?", (blog_post.title, blog_post.content, blog_post.date, blog_post_id ))
    conn.commit()
    return {"id": blog_post_id, "title": blog_post.title, "content": blog_post.content, "date": blog_post.date}

@app.delete("/blog-posts/{blog_post_id}")
def delete_blog_post(blog_post_id: int):
    cursor.execute("DELETE from blog-posts WHERE id = ?", (blog_post_id))
    conn.commit()
    return{"message": "Blog post deleted successfully"}
