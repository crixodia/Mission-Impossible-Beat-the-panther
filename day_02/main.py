import sys
import json

def units_convert(value: float, prefix: str, unit: str, to_prefix: str, to_unit: str):
    conversion_factors = json.load(open('conversion_factors.json'))

    prefixes = conversion_factors.get("prefixes", {})
    units = conversion_factors.get("units", {})

    if prefix not in prefixes and prefix:
        print(f"Error: prefix {prefix} not found")
        sys.exit(1)

    if unit not in units:
        print(f"Error: unit {unit} not found")
        sys.exit(1)

    if to_prefix not in prefixes and to_prefix:
        print(f"Error: prefix {to_prefix} not found")
        sys.exit(1)

    if to_unit not in units:
        print(f"Error: unit {to_unit} not found")
        sys.exit(1)

    if units.get(unit, {}).get("category") != units.get(to_unit, {}).get("category"):
        print(f"Error: units {unit} and {to_unit} are not compatible")
        sys.exit(1)

    to_prefix_scale = float(prefixes.get(to_prefix, {}).get("scale", 1))
    from_prefix_scale = float(prefixes.get(prefix, {}).get("scale", 1))
    to_scale = float(units.get(to_unit, {}).get("scale", 1))
    from_scale = float(units.get(unit, {}).get("scale", 1))

    return (value * from_scale * from_prefix_scale) / (to_scale * to_prefix_scale)


if __name__ == "__main__":
    value = float(input("Enter value [float]: "))
    prefix = input("Enter prefix [str]: ")
    unit = input("Enter unit [str]: ")
    to_prefix = input("Prefix to convert [str]: ")
    to_unit = input("Unit to convert [str]: ")

    result = units_convert(value, prefix, unit, to_prefix, to_unit)
    print(f"{value} {prefix}{unit} = {result} {to_prefix}{to_unit}")
