from django import forms
from mainapp.models import OrderHeaders, OrderDetails


class OrderHeadersEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = OrderHeaders
        fields = "__all__"


class OrderDetailsEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderDetailsEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = OrderDetails
        fields = "__all__"
