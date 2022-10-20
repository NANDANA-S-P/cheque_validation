from django.db import models


class UserbankInfo(models.Model):
    accNo = models.CharField(max_length = 20,null=True,blank=True)
    accHolderName = models.CharField(max_length = 20,null=True,blank=True)
    signature = models.ImageField(null=True,blank=True)
    phoneNumber = models.PositiveBigIntegerField(null=True,blank=True)
    balance = models.PositiveIntegerField(null=True,blank=True)

class Cheque(models.Model):
    chequeImage = models.ImageField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    chequeNo = models.PositiveIntegerField(null=True,blank=True)
    micrCode = models.PositiveIntegerField(null=True,blank=True)
    rbiAccNo = models.PositiveIntegerField(null=True,blank=True)
    transactionCode = models.PositiveIntegerField(null=True,blank=True)
    accHolder = models.ForeignKey(UserbankInfo,null=True,blank=True,on_delete=models.CASCADE)

class Transaction(models.Model):
    STATUS_CHOICES = (
        ("Success","Success"),
        ("Failed","Failed"),
        ("Bounced","Bounced"),
    )
    cheque = models.ForeignKey(Cheque,null=True,blank=True,on_delete=models.CASCADE)
    accNo = models.ForeignKey(UserbankInfo,null=True,blank=True,on_delete=models.CASCADE)
    receiver = models.CharField(max_length = 20,null=True,blank=True)
    status = models.CharField(max_length = 20,choices=STATUS_CHOICES,null=True,blank=True)
    amount = models.PositiveIntegerField(null=True,blank=True)