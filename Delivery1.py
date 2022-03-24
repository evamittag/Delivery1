import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#DATA import

Excel_file = 'delivery/my_shop_data.xlsx'
customers = pd.read_excel(Excel_file, "customers")
order = pd.read_excel(Excel_file, "order")
employee = pd.read_excel(Excel_file, "employee")
products = pd.read_excel(Excel_file, "products")

#Create charts

def customers():
    fig = px.pie(customers, values='Total', names='ProductName', title='Top 5 Products')
    return fig

def order():
    fig = px.pie(order, values='Total', names='CompanyName', title='Top 5 Customers')
    return fig

def employee():
    fig = px.bar(employee, x='EmployeesName', y='Total', title='Sales by Employees')
    return fig    

def products():
    fig = px.bar(products, x='CategoryName', y='Total', title='Category Sales')
    return fig
    