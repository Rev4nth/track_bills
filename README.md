Django implementation of simplebills

Create Virutal environment using virtualenv

Install Dependencies
--------------------------
pip install -r requirements.txt

Run the application locally
--------------------------
python manage.py runserver

Running DB migrations
----------------------
python manage.py makemigrations
python manage.py migrate


updated_bill = account_each.bill_set.get(pk=bill_id)
      updated_bill.title = bill_form.cleaned_data['bill_title']
      updated_bill.amount = bill_form.cleaned_data['bill_amount']
      updated_bill.date =  bill_form.cleaned_data['bill_date']
      updated_bill.image =  bill_form.cleaned_data['bill_image']
      updated_bill.save()
