from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    item.delete()
    return redirect('cart:view_cart')

@login_required
def update_cart_quantity(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, pk=item_id, user=request.user)
        item.quantity = int(request.POST.get('quantity', 1))
        item.save()
    return redirect('cart:view_cart')
