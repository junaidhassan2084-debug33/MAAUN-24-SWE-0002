from models import FuelDispenser, CarWash

def main():
    """Main function to run the Station Manager"""
    
    # Create a list of different station assets
    assets = [
        FuelDispenser(fuel_price=5.50, liters_dispensed=500),
        FuelDispenser(fuel_price=5.50, liters_dispensed=750),
        CarWash(wash_price=15.00, number_of_washes=120),
        CarWash(wash_price=20.00, number_of_washes=85),
        FuelDispenser(fuel_price=5.50, liters_dispensed=600),
    ]
    
    print("="*50)
    print("     STATION MANAGER - REVENUE CALCULATOR")
    print("="*50)
    print()
    
    # Calculate and display individual asset revenues
    total_revenue = 0
    
    for i, asset in enumerate(assets, 1):
        asset_type = type(asset).__name__
        revenue = asset.calculate_revenue()
        total_revenue += revenue
        
        if isinstance(asset, FuelDispenser):
            print(f"{i}. {asset_type}")
            print(f"   Price per liter: ${asset.fuel_price:.2f}")
            print(f"   Liters dispensed: {asset.liters_dispensed}")
            print(f"   Revenue: ${revenue:.2f}")
        elif isinstance(asset, CarWash):
            print(f"{i}. {asset_type}")
            print(f"   Price per wash: ${asset.wash_price:.2f}")
            print(f"   Number of washes: {asset.number_of_washes}")
            print(f"   Revenue: ${revenue:.2f}")
        
        print()
    
    # Display total station revenue
    print("="*50)
    print(f"TOTAL STATION REVENUE: ${total_revenue:.2f}")
    print("="*50)


if __name__ == "__main__":
    main()