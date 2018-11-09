from django.views.generic.detail import DetailView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView


from myapp_01 import models


class ADetailView(DetailView):
    model = models.A


class BInline(InlineFormSetFactory):
    model = models.B
    fields = '__all__'


class CInline(InlineFormSetFactory):
    model = models.C
    fields = '__all__'


class ACreateView(CreateWithInlinesView):
    model = models.A
    inlines = [BInline, CInline]
    fields = '__all__'

    def get_success_url(self):
        return self.object.get_absolute_url()


class AUpdateView(UpdateWithInlinesView):
    model = models.A
    #form_class = OrderForm
    inlines = [BInline, CInline]

    def get_success_url(self):
        return self.object.get_absolute_url()
