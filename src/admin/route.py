# admin/route.py

from flask import Blueprint, render_template, request, redirect, url_for

admin_route = Blueprint('admin', __name__, template_folder='templates')

