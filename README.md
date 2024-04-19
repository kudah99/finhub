
![GitHub issues](https://img.shields.io/github/issues/kudah99/medsearch)
![GitHub License](https://img.shields.io/github/license/kudah99/medsearch)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kudah99/medsearch">
    <img src="media/images/android-chrome-512x512.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">MedSearch</h3>

  <p align="center">
    MedSearch is a user-friendly online platform designed to facilitate the seamless discovery 
    of medical specialists and healthcare facilities. This platform employs
     advanced artificial intelligence to provide an efficient and personalized 
     experience for users seeking healthcare professionals based on specific 
     conditions or symptoms.
    <br />
    <br />
    <br />
    <a href="https://www.medsearch.co.zw">View Site</a>
    ·
    <a href="https://github.com/kudah99/medsearch/issues">Report Bug</a>
    ·
    <a href="https://github.com/kudah99/medsearch/issues">Request Feature</a>
  </p>
</div>
<img src="media/images/screenshot.png" alt="screenshot" width="100%" height="100%">

### Built With

- ![PyPI - Version](https://img.shields.io/pypi/v/django?style=flat&label=Django)
- ![NPM Version](https://img.shields.io/npm/v/tailwindcss?label=Tailwindcss)
- ![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fnumpy%2Fnumpy%2Fmain%2Fpyproject.toml)
- ![NPM Version](https://img.shields.io/npm/v/alpinejs?label=Alpine%20js)
- ![Static Badge](https://img.shields.io/badge/Database-postgresql-green)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kudah99/medsearch.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Setup environment variables `.env`. Below is an example `.env` file

   ```py
   DB_NAME=postgres
   DB_USER=user
   DB_PASSWORD=123
   DB_HOST=127.0.0.1
   DB_PORT=5432
   DB_ENGINE=postgresql
   SECRET_KEY=your-django-key
   DEBUG=True

   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Kudakwashe Chris Chipangura - [@kudachipangura](https://twitter.com/kudachipangura)

Project Link: [https://github.com/kudah99/medsearch](https://github.com/kudah99/medsearch)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Free Hosting By Vercel](https://vercel.com/)
- [Free Postgreql Database Hosting](https://www.elephantsql.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

To create a filterable list using Tailwind CSS and JavaScript with "chips" (tag-like filters), and assuming the data is being loaded from a Django backend, you'll follow these general steps:

1. **Setup your Django backend to serve the data.** This might be in the form of a REST API using Django REST Framework, or through server-rendered Django templates.

2. **Create the HTML structure with Tailwind CSS for styling.**

3. **Write JavaScript to handle the filter logic based on selected chips.**

Here's a step-by-step guide to achieve this:

### 1. Django Setup (Optional REST API Example)

You could use Django REST Framework to create an API that your frontend can query to get the data. Here’s a simple model and API setup:

```python
# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

# serializers.py
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'category']

# views.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### 2. HTML & Tailwind CSS

Let's create a simple page layout using Tailwind CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <title>Filterable List</title>
</head>
<body>
    <div class="p-5">
        <div id="chips" class="flex flex-wrap gap-2">
            <!-- Chips will be dynamically inserted here -->
        </div>
        <ul id="itemList" class="mt-5">
            <!-- Items will be listed here -->
        </ul>
    </div>

    <script src="main.js"></script>
</body>
</html>
```

### 3. JavaScript for Dynamic Loading and Filtering

Create a `main.js` file to handle fetching data, rendering chips, and filtering the list:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = '/api/items/';
    let items = [];
    let filters = new Set();

    const fetchItems = async () => {
        const response = await fetch(apiUrl);
        const data = await response.json();
        items = data;
        renderItems(items);
        renderChips();
    };

    const renderItems = (itemsToRender) => {
        const itemList = document.getElementById('itemList');
        itemList.innerHTML = '';
        itemsToRender.forEach(item => {
            itemList.innerHTML += `<li class="border p-2">${item.name}</li>`;
        });
    };

    const renderChips = () => {
        const chipContainer = document.getElementById('chips');
        const categories = [...new Set(items.map(item => item.category))];
        chipContainer.innerHTML = '';
        categories.forEach(category => {
            const chip = document.createElement('button');
            chip.textContent = category;
            chip.className = 'bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded';
            chip.onclick = () => toggleFilter(category);
            chipContainer.appendChild(chip);
        });
    };

    const toggleFilter = (category) => {
        if (filters.has(category)) {
            filters.delete(category);
        } else {
            filters.add(category);
        }
        filterItems();
    };

    const filterItems = () => {
        if (filters.size === 0) {
            renderItems(items);
        } else {
            const filteredItems = items.filter(item => filters.has(item.category));
            renderItems(filteredItems);
        }
    };

    fetchItems();
});
```

### Explanation:
- **JavaScript:** This script fetches items from your Django API, dynamically creates filter chips for each category, and filters the displayed items based on selected chips.
- **CSS:** Tailwind is used for quick, utility-first styling.

**Note:** Ensure Tailwind CSS is included in your project, and you have set up CORS correctly if your frontend and backend are served from different origins. Adjust API URLs as necessary based on your actual setup.