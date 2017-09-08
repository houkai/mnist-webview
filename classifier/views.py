# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# Render landing page with canvas
def index(request, *args, **kwargs):
	return render(request, "index.html", {})
