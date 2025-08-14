
# Assignment 1: Design Your Own Class


class Smartphone:
    """A class representing a smartphone with various features"""
    
    def __init__(self, brand, model, storage_gb, battery_percentage=100):
        """Initialize smartphone attributes"""
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery = battery_percentage
        self.is_locked = True
        self.apps = []
    
    def unlock(self, pin):
        """Unlock the phone with correct PIN"""
        if pin == "1234":  # Simple hardcoded PIN for demonstration
            self.is_locked = False
            return "Phone unlocked"
        return "Wrong PIN"
    
    def install_app(self, app_name, app_size):
        """Install an app if there's enough storage"""
        if self.storage_gb >= app_size:
            self.apps.append(app_name)
            self.storage_gb -= app_size
            return f"{app_name} installed successfully"
        return "Not enough storage space"
    
    def charge(self, percentage):
        """Charge the phone battery"""
        self.battery = min(100, self.battery + percentage)
        return f"Battery now at {self.battery}%"
    
    def __str__(self):
        """String representation of the phone"""
        return f"{self.brand} {self.model} with {self.storage_gb}GB storage, Battery: {self.battery}%"

# Inheritance example
class PremiumSmartphone(Smartphone):
    """A premium smartphone with additional features"""
    
    def __init__(self, brand, model, storage_gb, has_stylus=False):
        """Initialize with additional premium features"""
        super().__init__(brand, model, storage_gb)
        self.has_stylus = has_stylus
        self.water_resistant = True
    
    def use_stylus(self):
        """Use the stylus if available"""
        if self.has_stylus:
            return "Using stylus for precision input"
        return "This model doesn't have a stylus"
    
    def unlock(self, pin):
        """Override unlock with face recognition option"""
        if pin == "face":
            self.is_locked = False
            return "Unlocked with face recognition"
        return super().unlock(pin)





# Assignment 2: Polymorphism Challenge





class Animal:
    """Base class for all animals"""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Generic movement method to be overridden"""
        return f"{self.name} is moving"

class Fish(Animal):
    """Fish class that inherits from Animal"""
    
    def move(self):
        """Fish-specific movement"""
        return f"{self.name} is swimming 🐟"

class Bird(Animal):
    """Bird class that inherits from Animal"""
    
    def move(self):
        """Bird-specific movement"""
        return f"{self.name} is flying ✈️"

class Snake(Animal):
    """Snake class that inherits from Animal"""
    
    def move(self):
        """Snake-specific movement"""
        return f"{self.name} is slithering 🐍"

# ======================
# Demonstration Code
# ======================

if __name__ == "__main__":
    print("=== Assignment 1 Demonstration ===")
    
    # Create a regular smartphone
    my_phone = Smartphone("Samsung", "Galaxy S20", 128)
    print(my_phone)
    print(my_phone.unlock("1234"))
    print(my_phone.install_app("Camera", 2))
    print(my_phone.charge(30))
    
    # Create a premium smartphone
    premium_phone = PremiumSmartphone("Samsung", "Galaxy Note", 256, True)
    print("\nPremium phone features:")
    print(premium_phone.use_stylus())
    print(premium_phone.unlock("face"))
    
    print("\n=== Assignment 2 Demonstration ===")
    
    # Create different animals
    animals = [
        Fish("Nemo"),
        Bird("Eagle"),
        Snake("Viper")
    ]
    
    # Demonstrate polymorphism
    for animal in animals:
        print(animal.move())