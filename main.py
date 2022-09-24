from models.models import Employee, Plant

while True:
    print("1. Add new Plant\n" + 
          "2. Get all Plants\n" +
          "3. Get Plant by Id\n" +
          "4. Add new employee\n" +
          "5. Get all employees\n" +
          "6. Get employee by Id"
          )
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plant name: ")
        location = input("Plant location: ")
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        Plant.get_all_plants()
    elif flag == 3:
        id = int(input("Type id to search: "))
        Plant.get_by_id(id)
    elif flag == 4:
        name = input("Employee name: ")
        plant_id = input("Employee plant_id: ")
        employee = Employee(name, plant_id)
        employee.save()
    elif flag == 5:
        Employee.get_all_employees()
    elif flag == 6:
        id = int(input("Type id to search: "))
        Employee.get_by_id(id)

