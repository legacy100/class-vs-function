from django.shortcuts import render, redirect
from . models import Products
from django.views import View
from . forms import ProductForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class Index(View):
    def get(self, request):
        products = Products.objects.all().order_by('-created')
        return render(request, 'index.html', {'products': products})


    def post(self, request):
        product = Products.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            image_url=request.POST.get('image_url'),
        )
        product.save()
        return redirect('index')

class CreateProduct(CreateView):
    # model = Products
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = '/'

    # fields = ['name', 'price', 'stock', 'image_url']
    # def get(self, request):
    #     product = ProductForm()
    #     return render(request, 'create_product.html', {'product':product})


    # def post(self, request):
    #     form = ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')

            
class UpdateProduct(UpdateView):
    model = Products
    fields = ['name', 'price', 'stock', 'image_url']
    def get(self, request, pk):
        product = Products.objects.get(id=pk)
        content = {'product':product}
        return render (request, 'update_product.html', content)

    
    def post(self, request, pk):
        product= Products.objects.get(id=pk)
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.image_url = request.POST.get('image_url')
        product.save()
        return redirect('index')


class DeleteProduct(DeleteView):
    model = Products
    success_url: reverse_lazy('product-detail')

    
            