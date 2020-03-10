from django.forms import ModelForm
from django import forms
from .models import Order


class OrderForm(ModelForm):
    
    OPTIONS = (
        ('',''),
        ('Yes','Y'),
        ('No','N'),
    )
    
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    OPTIONS3 = (
        ('',''),
        ('O','O'),
        ('S','S'),
    )
    OPTIONS4 = (
        ('',''),
        ('A','A'),
        ('R','R'),
    )
    OPTIONS5 = (
        ('',''),
        ('RE','RE'),
        ('CM','CM'),
    )
    OPTIONS6 = (
        ('',''),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
    )


    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    order_received = forms.ChoiceField(choices=OPTIONS)
    price_method = forms.ChoiceField(choices=OPTIONS3)
    surcharge = forms.ChoiceField(choices=OPTIONS)
    A_R_credit = forms.ChoiceField(choices=OPTIONS4)
    fax_ASN = forms.ChoiceField(choices=OPTIONS)
    email_ASN = forms.ChoiceField(choices=OPTIONS)
    order_type = forms.ChoiceField(choices=OPTIONS5)

    class Meta:
        model = Order
        fields = ['purchase_order','bill_address','ship_address','required_date','freight','quote','contract','order_status',
                  'order_received', 'price_method', 'surcharge', 'A_R_credit', 'fax_ASN', 'email_ASN', 'order_type',
                  'order_number', 'order_type', 'ordered_date', 'price_details', 'kit_details', 'ship_via', 'attention',
                  'ship_instructions', 'F_O_B', 'warehouse', 'sales_rep', 'product_line', 'COS_project', 'sales_account',
                  'order_value', 'staus_number', 'contact_name', 'phone_number', 'ship_cond', 'credit_control', 'ASN_contact',
                  'ASN_title', 'ASN_fax_num', 'email_addr']
    
