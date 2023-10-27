# CRUD

## Insert
Three methods

### Simply Using Constructor

```
Product(values);
```

### Using `objects.create`

```
 Product.objects.create(name="Nexus" , price=10534)
```

### Using Dictornary `**` operator

```
Product.objects.create(**dict_obj)
```

### Update the Data

```
Product.objects.filter(id=2).update(name="Kia Seltos II") 
```
## OR

```
car = Product.objects.get(id=2)
car.name = 'Kia Seltos' 
```

### Delete the Instance

```
Product.objects.filter(id=2).delete()
```

# ORM
- OrderBy: Recipe.objects.all().order_by('-view_count 
    ...: ') For Decending Order

- OrderBy: Recipe.objects.all().order_by('view_count 
    ...: ') For Ascending Order

- vege = Recipe.objects.all().order_by('view_count' 
    ...: )[0:1] (Here `[0:1]` tells that we limit the response and we want only 1 item)

- Recipe.objects.filter(view_count__gte=55) : Here gte means greater and equal to

# Foreign Key Access

### queryset = Student.objects.filter(dept__department = "Maths")
- Here the `dept` is the foreign key and `department` is the attribute of the model `Department`. Here is to add the filters *dept__department__icontains*

### query = Student.objects.exclude(dept__department = "Maths") 
- It is used to exclude the objects from the queryset.

### query.exits() : means it is used to check whether the object exists or not.

### query.values(): It will serialize the data or we say it will convert the queryset into json like

### query().reverse(): It will reverse the queryset


# Agreegate Functions

```cmd
In [41]: query = Student.objects.aggregate(Avg('student_age'))

In [42]: query
Out[42]: {'student_age__avg': 25.387096774193548}

In [43]: Student.objects.aggregate(Max('student_age'))
Out[43]: {'student_age__max': 30}

In [44]: Student.objects.aggregate(Min('student_age'))
Out[44]: {'student_age__min': 18}

In [45]: Student.objects.aggregate(Sum('student_age'))
Out[45]: {'student_age__sum': 787}
```








