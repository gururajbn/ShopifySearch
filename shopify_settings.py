# Replace the API Key and Shared Secret with the one given for your
# App by Shopify.
#
# To create an application, or find the API Key and Secret, visit:
# - for private Apps:
#     https://${YOUR_SHOP_NAME}.myshopify.com/admin/api
# - for partner Apps:
#     https://www.shopify.com/services/partners/api_clients
#
# You can ignore this file in git using the following command:
#   git update-index --assume-unchanged shopify_settings.py
import os
SHOPIFY_API_KEY = '441ea973abec33c5cc1825e1b123a3ed'
SHOPIFY_API_SECRET ='fddfd7319418c22cc4692d3ac81e914f'

# See http://api.shopify.com/authentication.html for available scopes
# to determine the permisssions your app will need.
SHOPIFY_API_SCOPE = ['read_products', 'read_orders','read_customers']
