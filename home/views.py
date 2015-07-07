from django.shortcuts import render
from django.views.generic import View
import shopify
import datetime
today = datetime.datetime.now()
diff= today -datetime.timedelta(days=365)
yearago = diff.strftime("%Y-%m-%d")+" 00:00"



class home(View):

    def get(self,request): 
        return render(request,"home/home.html",{
                    'product_count':shopify.Product.count(),
                    'order_count':shopify.Order.count(),
                    'customer_count': shopify.Customer.count(),
                })

    def post(self,request):
        
        title=request.POST['product']
        product_list=shopify.Product.find(title=title)

        if not product_list:
            message="No Product found"
        else:
            message="%d Product containing \'%s\' found" %(len(product_list),title)

        return render(request,"home/home.html",{
                    'products':product_list,
                    'message':message,
                    'product_count': shopify.Product.count(),
                    'order_count':shopify.Order.count(),
                    'customer_count': shopify.Customer.count(),
                })

class Order(View):

    def get(self,request,pk):
        product= shopify.Product.find(pk)
        order_list=shopify.Order.find(created_at_min=yearago)
        customers_list=[]
        print product.id,product.title
        print order_list

        for order in order_list:
            for p in order.line_items:
                if product.id == p.product_id:
                    customers_list.append(order.customer)

        print customers_list
        return render(request, "home/order.html",{
            'product':product,
            'customers':customers_list,
            })

