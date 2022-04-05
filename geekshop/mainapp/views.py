from django.shortcuts import render

def index(request):
  context = {
    "title_logo": "GeekShop",
    "title": "GeekShop Store"
  }
  return render(request, "mainapp/index.html", context=context)

def products(request):
  context = {
    "title_logo": "GeekShop",
    "title": "GeekShop - Каталог",
    "categories": [
      {"name": "Новинки"},
      {"name": "Одежда"},
      {"name": "Обувь"},
      {"name": "Аксессуары"},
      {"name": "Подарки"}
    ],
    "products": [
      {"name": "Худи черного цвета с монограммами adidas Originals",
       "prise": 6090,
       "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
       "img_url": "vendor/img/products/Adidas-hoodie.png"},
      {"name": "Синяя куртка The North Face",
       "prise": 23725,
       "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
       "img_url": "vendor/img/products/Blue-jacket-The-North-Face.png"},
      {"name": "Коричневый спортивный oversized-топ ASOS DESIGN",
       "prise": 3390,
       "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
       "img_url": "vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png"},
      {"name": "Черный рюкзак Nike Heritage",
       "prise": 2340,
       "description": "Плотная ткань. Легкий материал.",
       "img_url": "vendor/img/products/Black-Nike-Heritage-backpack.png"},
      {"name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
       "prise": 13590,
       "description": "Гладкий кожаный верх. Натуральный материал.",
       "img_url": "vendor/img/products/Black-Dr-Martens-shoes.png"},
      {"name": "Темно-синие широкие строгие брюки ASOS DESIGN",
       "prise": 2890,
       "description": "Легкая эластичная ткань сирсакер Фактурная ткань.",
       "img_url": "vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png"},
    ]
  }
  return render(request, "mainapp/products.html", context=context)
