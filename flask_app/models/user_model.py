import email
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into users (email) VALUES (%(email)s);"
        return connectToMySQL('email_schema').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('email_schema').query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod # here we just need the id of the line item we are going to delete
    def destroy(cls, id):
        query = f"DELETE FROM users WHERE id = {id};"
        return connectToMySQL('email_schema').query_db(query)

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('email_schema').query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        return is_valid