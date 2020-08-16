from mainapp.models import OrderHeaders, OrderDetails
from django.db.models import F, OuterRef, Subquery
from mainapp.forms import OrderHeadersEditForm, OrderDetailsEditForm
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy


def main(request):
    title = "Tables"
    order_headers_list = OrderHeaders.objects.all()
    order_details_list = OrderDetails.objects.all()
    content = {"title": title,
               "headers": order_headers_list,
               "details": order_details_list}
    return render(request, "mainapp/index.html", content)


def select(request):
    costly = OrderDetails.objects.filter(
        hdr=OuterRef('pk')).annotate(cost=F('price') * F('amount')).order_by('-cost', '-price')[:1]
    items_pk = [el.item_pk for el in OrderHeaders.objects.annotate(item_pk=Subquery(costly.values('pk')))]
    items = OrderDetails.objects.filter(pk__in=items_pk).select_related().annotate(cost=F('price') * F('amount'))
    context = {'items': items}
    return render(request, 'mainapp/select.html', context)


def order_header(request):
    title = "Главная заказов"
    order_header_list = OrderHeaders.objects.all()
    content = {"title": title,
               "objects": order_header_list
               }
    return render(request, "mainapp/orderheader.html", content)


class OrderHeadersCreateView(CreateView):
    model = OrderHeaders
    template_name = "mainapp/orderheader_update.html"
    success_url = reverse_lazy("order_header")
    fields = "__all__"


class OrderHeadersUpdateView(UpdateView):
    model = OrderHeaders
    template_name = "mainapp/orderheader_update.html"
    success_url = reverse_lazy("order_header")
    form_class = OrderHeadersEditForm

    def get_context_data(self, **kwargs):
        context = super(OrderHeadersUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Редактирование заказа"
        return context


class OrderHeadersDeleteView(DeleteView):
    model = OrderHeaders
    template_name = "mainapp/orderheader_delete.html"
    success_url = reverse_lazy("order_header")


def order_details(request, pk):
    title = "Детали заказа"
    headers = get_object_or_404(OrderHeaders, pk=pk)
    orderd_details_list = OrderDetails.objects.filter(hdr__pk=pk).order_by("pk")
    content = {"title": title,
               "headers": headers,
               "objects": orderd_details_list}
    return render(request, "mainapp/orderdetails.html", content)


class OrderDetailsCreateView(CreateView):
    model = OrderDetails
    template_name = "mainapp/orderdetails_update.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('order_details', args=[self.headers.pk])

    def get_context_data(self, **kwargs):
        self.headers = get_object_or_404(OrderHeaders, pk=self.kwargs['pk'])
        kwargs['headers'] = self.headers
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.headers = get_object_or_404(OrderHeaders, pk=self.kwargs['pk'])
        form.instance.headers = self.headers
        return super().form_valid(form)


def order_details_update(request, pk):
    title = "Обновить элемент заказа"
    edit_order_details = get_object_or_404(OrderDetails, pk=pk)

    if request.method == "POST":
        edit_form = OrderDetailsEditForm(request.POST, request.FILES, instance=edit_order_details)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("order_details_update", args=[edit_order_details.pk]))
    else:
        edit_form = OrderDetailsEditForm(instance=edit_order_details)

    content = {
        "title": title,
        "form": edit_form,
        "headers": edit_order_details.hdr,
    }
    return render(request, "mainapp/orderdetails_update.html", content)


def order_details_delete(request, pk):
    title = "Удалить элемент заказа"
    details = get_object_or_404(OrderDetails, pk=pk)

    if request.method == "POST":
        details.is_active = False
        details.save()
        return HttpResponseRedirect(reverse("order_details", args=[details.hdr.pk]))

    content = {"title": title,
               "product_to_delete": details
               }
    return render(request, "mainapp/orderdetails_delete.html", content)



