from django.db import models

# Create your models here.
class Order (models.Model):
    purchase_order = models.IntegerField(blank=False, null=False);
    bill_address = models.TextField(blank=True);
    ship_address = models.TextField(blank=True);
    required_date = models.DateField(blank=False);
    freight = models.CharField(max_length=50);
    quote = models.CharField(max_length=50);
    contract= models.IntegerField(blank=False, null=False);
    order_status = models.CharField(max_length=50);

    order_received = models.CharField(max_length=50);
    price_method = models.CharField(max_length=50);
    surcharge = models.CharField(max_length=50);
    A_R_credit = models.CharField(max_length=50);
    fax_ASN = models.CharField(max_length=50);
    email_ASN = models.CharField(max_length=50);
    order_type = models.CharField(max_length=50);


    order_number = models.IntegerField(default=False, blank=True, null=True);
    ordered_date = models.DateField(blank=True, null=False);
    price_details = models.TextField(blank=True, null=False);
    kit_details = models.TextField(blank=True, null=False);
    ship_via = models.TextField(blank=True, null=False);
    attention = models.TextField(blank=True, null=False);
    ship_instructions = models.TextField(blank=True, null=False);
    F_O_B = models.TextField(blank=True, null=False);
    warehouse = models.IntegerField(blank=True, null=True);
    sales_rep = models.CharField(max_length=50, blank=True, null=False);
    product_line = models.TextField(blank=True, null=False);
    COS_project = models.IntegerField(blank=True, null=True);
    sales_account = models.IntegerField(blank=True, null=True);
    order_value = models.IntegerField(blank=True, null=True);
    staus_number = models.IntegerField(blank=True, null=True);
    contact_name = models.CharField(max_length=50, blank=True);
    phone_number = models.IntegerField(blank=True, null=True);
    ship_cond = models.IntegerField(blank=True, null=True);
    credit_control = models.IntegerField(blank=True, null=True);
    ASN_contact = models.TextField(blank=True, null=False);
    ASN_title = models.TextField(blank=True, null=False);
    ASN_fax_num = models.IntegerField(blank=True, null=True);
    email_addr = models.CharField(max_length=50, blank=True);
     

class Line(models.Model):
    order_number = models.IntegerField(default=False, blank=True, null=True);
    customer_number = models.IntegerField(default=False, blank=True, null=True); 
    customer_name = models.CharField(max_length=50, blank=True, null=True);
    cat = models.IntegerField(default=False, blank=True, null=True); 
    ship_days = models.IntegerField(default=False, blank=True, null=True); 
    travel_days = models.IntegerField(default=False, blank=True, null=True); 
    order_total = models.IntegerField(default=False, blank=True, null=True); 
    estimated_costs = models.IntegerField(default=False, blank=True, null=True);
    
    line_number = models.IntegerField(default=False, blank=False, null=True); 
    part_number = models.IntegerField(default=False, blank=False, null=True); 
    description = models.TextField(blank=True, null=False);
    whse = models.IntegerField(blank=True, null=True);
    alloc = models.TextField(blank=True, null=False);
    qty_order = models.IntegerField(default=False, blank=False, null=True); 
    qty_avail = models.IntegerField(default=False, blank=True, null=True); 
    required_date = models.DateField(blank=False);
    promised_date = models.DateField(blank=True);
    unit_price = models.FloatField(default=False, blank=False, null=True)
    ship_tolerance_min = models.IntegerField(default=False, blank=True, null=True); 
    ship_tolerance_max = models.IntegerField(default=False, blank=True, null=True); 
    uos = models.IntegerField(default=False, blank=True, null=True); 
    price_book = models.IntegerField(default=False, blank=True, null=True); 
    stat = models.CharField(max_length=50);








 
