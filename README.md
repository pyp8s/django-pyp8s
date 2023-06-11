# django-pyp8s

Django application for pyp8s — customisable prometheus exporter for your python application.

## Installation

```bash
python3 -m pip install django-pyp8s
```

## Usage

Examples: [https://github.com/pyp8s/examples](https://github.com/pyp8s/examples)

### urls.py

```python
from django.urls import path, include

urlpatterns += [
    path('', include('django_pyp8s.urls')),
]
```

### settings.py

```python
INSTALLED_APPS += [
    django_pyp8s,
]
```

## Reporting bugs

Please, use GitHub issues.

## Requesting new functionality

Please, use GitHub issues.
