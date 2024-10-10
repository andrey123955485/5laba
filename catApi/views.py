from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CatImage
import random
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def random_cat(request, count=1):
    cat_images = CatImage.objects.all()
    random_images = random.sample(list(cat_images), min(count, cat_images.count()))
    if count == 1:
        return Response({"source": request.build_absolute_uri(random_images[0].image.url)})
    else:
        sources = [request.build_absolute_uri(cat.image.url) for cat in random_images]
        return Response({"source": sources})

from django.shortcuts import render

from django.shortcuts import render
from .models import CatImage

def home(request):
    images = CatImage.objects.all()
    return render(request, 'catApi/home.html', {'images': images})

