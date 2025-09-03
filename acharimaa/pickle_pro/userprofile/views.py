from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest 
from .models import CustomUser
from django.core.mail import send_mail
from .models import Cart, CartItem, ContactUs 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from .models import Checkout, CheckoutProduct, Cart
from .models import Cart, Checkout, CheckoutProduct
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Checkout
import threading
import random
import json
import ipdb

def home(request):
    mango_product = MangoProduct.objects.order_by('-id').first()
    lemon_product = LemonProduct.objects.order_by('-id').first()
    mixed_product = MixedProduct.objects.order_by('-id').first()
    panjabi_product = PanjabiProduct.objects.order_by('-id').first()
    kerda_product = KerdaProduct.objects.order_by('-id').first()
    carrot_product = CarrotProduct.objects.order_by('-id').first()
    images = CarouselImage.objects.all() 
    
    cart_count = 0
    try:
        if request.user.is_authenticated:
            cart_count = CartItem.objects.filter(cart__user=request.user).count()
    except Exception as e:
        print(f"Cart count error: {e}")
        cart_count = 0

    context = {
        'mango_products': [mango_product] if mango_product else [],
        'lemon_products': [lemon_product] if lemon_product else [],
        'mixed_products': [mixed_product] if mixed_product else [],
        'panjabi_products': [panjabi_product] if panjabi_product else [],
        'kerda_products': [kerda_product] if kerda_product else [],
        'carrot_products': [carrot_product] if carrot_product else [],
        'cart_count': cart_count,
        'images': images,
    }

    return render(request, 'home.html', context)

def mango(request):
    mango_products = MangoProduct.objects.all()
    mango_products = MangoProduct.objects.filter(is_available=True)
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'mango_products': mango_products, 
        'cart_count': cart_count,
    }
    return render(request, 'mango.html', context)

def Lemon(request):
    lemon_products = LemonProduct.objects.all()
    lemon_products = LemonProduct.objects.filter(is_available=True)
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'lemon_products': lemon_products,
        'cart_count': cart_count,
    }
    return render(request,'Lemon.html', context)

def Mixed(request):
    mixed_products = MixedProduct.objects.all()
    mixed_products = MixedProduct.objects.filter(is_available=True)
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'mixed_products': mixed_products, 
        'cart_count': cart_count,
    }
    return render(request,'Mixed.html', context)

def Panjabi(request):
    panjabi_products = PanjabiProduct.objects.all()
    panjabi_products = PanjabiProduct.objects.filter(is_available=True)
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'panjabi_products': panjabi_products, 
        'cart_count': cart_count,
    }
    return render(request,'Panjabi.html', context)

def kerda(request):
    kerda_products = KerdaProduct.objects.all()
    kerda_products = KerdaProduct.objects.filter(is_available=True)
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = { 
        'kerda_products': kerda_products, 
        'cart_count': cart_count,
    }
    return render(request,'kerda.html', context)

def Carrot(request):
    carrot_products = CarrotProduct.objects.all()
    carrot_products = CarrotProduct.objects.filter(is_available=True)
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'carrot_products': carrot_products,
        'cart_count': cart_count,
    }
    return render(request,'Carrot.html', context)

def howwe(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request,'howwe.html',context)

def makeour(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request,'makeour.html',context)

def blogs(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request,'blogs.html',context)

def Contact(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request,'Contact.html',context)

def recipes(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request,'recipes.html',context)

def createaccount(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()

    context = {'cart_count': cart_count}

    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        if CustomUser.objects.filter(email=email).exists():
            context['account_exists'] = True  # add this flag
            return render(request, 'createaccount.html', context)

        created = CustomUser.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number
        )
        created.set_password(password)
        created.save()

        context['signup_success'] = True  # add this flag
        return render(request, 'createaccount.html', context)

    return render(request, 'createaccount.html', context)


def password(request):
    return render(request,'password.html')

@csrf_exempt
def send_otp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()

            # Send email
            send_mail(
                'Your OTP Code',
                f'Your OTP is: {otp}',
                'noreply@example.com',
                [email],
                fail_silently=False,
            )

            return JsonResponse({'status': 'OTP sent'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'Email not found'}, status=404)
    else:
        # Handle GET requests or other methods
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

@csrf_exempt
def verify_otp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        otp = data.get('otp')

        try:
            user = CustomUser.objects.get(otp=otp)
            return JsonResponse({'status': 'OTP verified'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'Invalid OTP'}, status=400)

@csrf_exempt
def reset_password(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if new_password != confirm_password:
            return JsonResponse({'status': 'Passwords do not match'}, status=400)

        otp = data.get('otp')
        try:
            user = CustomUser.objects.get(otp=otp)
            user.set_password(new_password)
            user.otp = None
            user.save()
            return JsonResponse({'status': 'Password reset successfully'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'Invalid OTP'}, status=400)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            user = authenticate(request, email=user.email, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'login.html', {'login_success': True})
            else:
                messages.error(request, 'Invalid email or password.')
                return redirect('login')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')                 
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')  

class EmailThread(threading.Thread):
    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=self.recipient_list,
            fail_silently=False,
        )

def checkout(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.items.all()

    cart_count = cart_items.count()
    total_price = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        full_name = request.POST.get('name') or user.full_name
        email = request.POST.get('email') or user.email
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone') or user.phone_number
        payment_method = request.POST.get('payment_method')

        if not all([full_name, email, address, city, phone, payment_method]):
            messages.error(request, 'All fields are required.')
            return render(request, 'checkout.html', {
                'cart': cart,
                'cart_items': cart_items,
                'total_price': total_price,
                'cart_count': cart_count,
                'user': user
            })

        # Save checkout
        checkout = Checkout.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            phone=phone,
            payment_method=payment_method,
            total=total_price
        )

        # Save checkout products
        for item in cart_items:
            product_instance = item.product
            content_type = ContentType.objects.get_for_model(product_instance)
            CheckoutProduct.objects.create(
                checkout=checkout,
                content_type=content_type,
                object_id=product_instance.pk,
                quantity=item.quantity,
                price=item.total_price()
            )

        # Clear the cart
        cart.items.all().delete()
        cart.delete()

        # Order history
        previous_orders = Checkout.objects.filter(email=email).order_by('-id')
        order_history_msg = ""
        for order in previous_orders:
            order_history_msg += f"\n🛒 Order #{order.id} - {order.order_status}\n"
            for item in order.checkout_products.all():
                # Check if product exists to avoid AttributeError
                product_name = item.product.name if item.product else "Product Unavailable"
                order_history_msg += f" - {item.quantity} x {product_name} (₹{item.price})\n"
            order_history_msg += f"Total: ₹{order.total}\n"

        # Customer email message
        customer_msg = f"""
        Dear {full_name},

        ✅ Your new order has been placed successfully!

        📦 Delivery Address:
        {address}, {city}
        📞 Phone: {phone}
        💳 Payment: {payment_method}

        💰 Total Price: ₹{total_price}

        📄 Order History:
        {order_history_msg}

        Thank you for shopping with us!
        - The Team
        """

        # Send customer email (in background)
        EmailThread(
            subject="✅ Order Confirmation & History",
            message=customer_msg,
            recipient_list=[email]
        ).start()

        # Admin email
        admin_msg = f"""
        New Order Received:

        Name: {full_name}
        Email: {email}
        Phone: {phone}
        Address: {address}, {city}
        Payment Method: {payment_method}
        Total Price: ₹{total_price}
        """

        # Send admin email (in background)
        EmailThread(
            subject="📥 New Order Received",
            message=admin_msg,
            recipient_list=[settings.EMAIL_HOST_USER]
        ).start()

        messages.success(request, '✅ Order placed successfully. Confirmation sent!')
        return redirect('thankyou')  # redirect to thank you page

    # GET request - render checkout page
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': cart_count,
        'user': user
    }
    return render(request, 'checkout.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Checkout, CartItem

@login_required
def order_complete(request):
    email = request.user.email
    previous_orders = Checkout.objects.filter(email=email).order_by('-id')
    cart_count = CartItem.objects.filter(cart__user=request.user).count()

    context = {
        'previous_orders': previous_orders,
        'email': email,
        'cart_count': cart_count,
        'login_required': False,  # optional, based on your template logic
    }

    return render(request, 'ordercomplete.html', context)

def invoice_view(request, order_id):
    order = get_object_or_404(Checkout, id=order_id)
    products = order.checkout_products.all()
    return render(request, 'invoice.html', {'order': order, 'products': products})

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUs

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Save to database
        ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Email to Admin
        admin_subject = f'New Contact Message from {name}'
        admin_message = f'Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}'
        send_mail(admin_subject, admin_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

        # Confirmation Email to User
        user_subject = 'Thanks for contacting us!'
        user_message = f"Hi {name},\n\nThanks for reaching out to us. We’ve received your message and will respond shortly.\n\nYour message:\n{message}"
        send_mail(user_subject, user_message, settings.EMAIL_HOST_USER, [email])

        return render(request, 'thankyou.html', {'name': name})
    return render(request, 'Contact.html')



def add_to_cart(request, product_type, product_id):
    user = request.user
    if not user.is_authenticated:
        messages.error(request, "You must be logged in to add items to the cart.")
        return redirect('createaccount')
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method")

    size = request.POST.get('size')
    if size not in ['250g', '500g', '1kg']:
        return HttpResponseBadRequest("Invalid size")

    product_type = product_type.lower()

    product_model_map = {
        'mango': MangoProduct,
        'lemon': LemonProduct,
        'mixed': MixedProduct,
        'kerda': KerdaProduct,
        'panjabi': PanjabiProduct,
        'carrot': CarrotProduct
    }

    product_model = product_model_map.get(product_type)
    if not product_model:
        return HttpResponseBadRequest("Invalid product type")

    product = get_object_or_404(product_model, id=product_id)

    price = getattr(product, f'price_{size}', None)
    if price is None:
        return HttpResponseBadRequest("Price not found for selected size")

    cart, _ = Cart.objects.get_or_create(user=request.user)

    content_type = ContentType.objects.get_for_model(product)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=product.id,
        size=size,
        defaults={'price': price, 'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} ({size}) added to your cart!")
    return redirect('cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')

def get_cart_items(request, product):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('content_type')  # Optional but good for performance

    cart_items_data = []
    total_price = 0
    product_model = {
        'mango': MangoProduct,
        'lemon': LemonProduct,
        'mixed': MixedProduct,
        'kerda': KerdaProduct,
        'panjabi': PanjabiProduct,
        'carrot': CarrotProduct,
    }.get(product)

    for item in items:
        product = item.product  # ✅ This is the correct way to access the actual product

        if not product:
            continue  # Skip broken items

        cart_items_data.append({
            'id': item.id,
            'name': product.name,
            'image': product.image.url if product.image else '',
            'price': product.price_250g,
            'quantity': item.quantity,
            'total_price': item.total_price()
        })

        total_price += item.total_price()

    return JsonResponse({
        'cart_items': cart_items_data,
        'total_price': total_price,
        "cart_count": cart.items.count()
    })

def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.items.all()
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    
    total_price = sum(item.total_price() for item in cart_items)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,        
        'cart_count': cart_count,
    }
    return render(request, 'cart.html', context)

def update_quantity(request, item_id, quantity):
    try:
        item = CartItem.objects.get(id=item_id)
        item.quantity = quantity
        item.save()
        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False}, status=404)

def thankyou(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request, 'thankyou.html', context)

def term_conditions(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request, 'term.html', context)

def privacypolicy(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'cart_count': cart_count,
    }
    return render(request, 'privacypolicy.html', context)