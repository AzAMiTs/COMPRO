def displa_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
displa_info(name="Alice",age=30,city="New York")