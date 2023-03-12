from django.conf import settings
from ecommerce.apps.catalog.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, qty):
        key = str(product.id)
        
        if key in self.cart:
            current_qty = self.cart[key]["qty"]
            self.cart[key]["qty"] = current_qty + qty
        else:
            self.cart[key] = {"qty": qty, "price": float(product.price)}

        self.save()


    def update(self, product_id, qty):
        key = str(product_id)

        if key in self.cart:
            self.cart[key]["qty"] = qty

        self.save()

    
    def delete(self, product_id):
        key = str(product_id)

        if key in self.cart:
            del self.cart[key]
            self.save()
    

    def __len__(self):
        return sum(item["qty"] for item in self.cart.values())


    def save(self):
        self.session.modified = True


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def __iter__(self):        
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:            
            cart[str(product.id)]["product"] = product            
            
        for item in cart.values():
            item["subtotal"] = item["product"].price * item["qty"]
            yield item
    

    def get_total(self):
        return sum(item["price"] * item["qty"] for item in self.cart.values())


        