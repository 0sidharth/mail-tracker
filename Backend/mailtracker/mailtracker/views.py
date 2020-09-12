from django.http import HttpResponse

import os.path
from django.views.generic import View


class PixelView(View):

    def get(self, request, *args, **kwargs):
        image_data = open('static/mailtracker/sk1.png', 'rb').read()
        unique_id = kwargs.get('unique_id')

       

        return HttpResponse(image_data, content_type="image/png")
