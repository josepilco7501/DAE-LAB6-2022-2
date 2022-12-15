from django.shortcuts import get_object_or_404, render


def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    context = {'product_list': product_list}
    return render(request, 'index.html', context)

def producto(request, product_id):
    producto = get_object_or_404(Producto, pk=product_id)
    return render(request, 'producto.html', {'producto':producto})
