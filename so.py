def naim(
    name: str,
    age: int,
    city: str = "Unknown",
    country: str = "Unknown"
) -> str:
    """
    This function takes a name, age, city, and country as input and returns a formatted string.
    
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    city (str): The city where the person lives. Default is "Unknown".
    country (str): The country where the person lives. Default is "Unknown".
    
    Returns:
    str: A formatted string containing the person's information.
    """
    return f"{name} is {age} years old and lives in {city}, {country}."