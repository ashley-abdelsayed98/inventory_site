# Inventory Site

## Requirements 
 
Please install python version 3.9+ https://realpython.com/installing-python/ 

Once python is installed, please install django in your command prompt or terminal: 
`pip install django`

Once python is installed, please clone or download this repository. 

# Run the project

Once this project is downloaded, execute this command in the `inventory_site` root folder of the project to run the project:

`[inventory_site]$ python manage.py runserver`
# How to use web app

First, navigate to the home page: http://127.0.0.1:8000/

From here you will be able to view all the available products in the inventory under the *All products* heading.

You can add a new product using the form at the top of the page.

Once you have added a product, click on it's name in the product list to view more details.

Here you can see all of the products information and whether or not it is in stock. But before you add stock for a product, you need to create a warehouse!

Click on the [*Warehouses*](http://127.0.0.1:8000/inventory/warehouses/) link in the navigation bar.

Here you can view all the existing warehouses and add a new warehouse.

After you have added a warehouse, navigate back to the [products ](http://127.0.0.1:8000/inventory/products/)page and select an item you would like to add stock for.

Now that you have a warehouse, you can click on the *Add stock* button to assign stock of a product to a warehouse.

On the product's detail page, you can also edit and delete the item.

You can also navigate to a specific warehouse's details page by clicking on it's name in the [list of warehouses](http://127.0.0.1:8000/inventory/warehouses/). Once there, you can edit or delete a warehouse. Be careful, if you delete a warehouse all the stock assigned to it dissapears!
