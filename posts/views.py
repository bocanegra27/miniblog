# posts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm # 1. Importa nuestro nuevo formulario

def post_list(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'posts/post_list.html', {'posts': posts})

# 2. Añade esta nueva vista
def post_create(request):
    # Si el método es POST, significa que el usuario ha enviado el formulario
    if request.method == 'POST':
        # Crea una instancia del formulario con los datos enviados (request.POST)
        form = PostForm(request.POST)
        # Django verifica si todos los datos son válidos
        if form.is_valid():
            # Si son válidos, guarda el objeto en la base de datos
            form.save()
            # Redirige al usuario a la lista de posts para ver su nueva creación
            return redirect('post_list')
    # Si el método es GET (el usuario solo está visitando la página)
    else:
        # Crea una instancia de un formulario vacío
        form = PostForm()
    
    # Renderiza la plantilla, pasándole el formulario como contexto
    return render(request, 'posts/post_form.html', {'form': form})

def post_update(request, pk):
    # Obtenemos el post que queremos editar usando su primary key (pk)
    # o mostramos una página 404 si no existe.
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # Al crear el formulario, le pasamos los datos del POST y
        # le decimos que es para la instancia del 'post' que ya obtuvimos.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        # Si es un GET, creamos el formulario pasándole la instancia del 'post'
        # para que los campos aparezcan rellenos con los datos actuales.
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form})

def post_delete(request, pk):
    # Obtenemos el post que queremos eliminar.
    post = get_object_or_404(Post, pk=pk)

    # Si el método es POST, significa que el usuario ha confirmado la eliminación.
    if request.method == 'POST':
        # Eliminamos el objeto de la base de datos.
        post.delete()
        # Redirigimos a la lista de posts.
        return redirect('post_list')

    # Si es GET, mostramos la página de confirmación.
    return render(request, 'posts/post_confirm_delete.html', {'post': post})