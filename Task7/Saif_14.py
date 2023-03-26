def make_car(manufacturer, model, **args):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    car.update(args)
    return car

car = make_car(name='audi', manufacturer = 'Volkswagen group',model ='Q8', color='Black')
print(car)

