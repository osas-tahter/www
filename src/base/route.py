# base/route.py

from flask import Blueprint, render_template, request, session, redirect, url_for
from base.model.user_model import UserModel
from base.service.menu_service import MenuService
from apps.route import app_route
from admin.route import admin_route

base_route = Blueprint('base', __name__, template_folder='templates')

# base_route.register_blueprint(app_route) #, url_prefix='/apps')
base_route.register_blueprint(admin_route, url_prefix='/admin')

def render_layout(type:int = 0):
    '''
    Render the layout based on the type of user.
    '''
    user_info = session.get('user')
    if user_info:
        user = UserModel(**user_info)
        menu = MenuService.get_menu(type)
        if type == 1: 
            route = request.args.get('route', "/admin/dashboard")
            template_name = 'admin.html'
        else:
            route = request.args.get('route', "/apps/dashboard")
            template_name = 'index.html'            
        print(f"Route: {route}")
        return render_template(template_name, user=user, route=route, menu=menu)
    else:
        return redirect(url_for('auth.login'))
    
@base_route.route('/')
def index():
    return render_layout(0)

@base_route.route('/admin')
def admin():
    return render_layout(1)

@base_route.route('/error')
def error():
    return render_template('error.html')
