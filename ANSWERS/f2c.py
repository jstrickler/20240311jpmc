import logging
from temp_conv import f2c

logging.basicConfig(
    filename="temp_conv.log",
    level=logging.DEBUG,   # log messages at level info and above (default: WARNING)
    format="%(levelname)s %(name)s %(asctime)s %(filename)s %(message)s",
    datefmt="%x-%X",
)

x = "my output"
print(x)
logging.info(x)
# or use multiple log handlers

logging.info("Starting Program")

temp_str = input("Enter Fahrenheit temp: ")
logging.debug("User entered %s", temp_str)

try:
    fahrenheit = float(temp_str)
    logging.debug("fahrenheit value %f", fahrenheit)
except (ValueError, TypeError) as err:
    logging.error("Invalid number: %s", temp_str)
    print("Invalid number", temp_str)
    exit()
except Exception as err:  # any error
    logging.critical("Unexpected error: %s", err)
else:  # if no errors...
    celsius = f2c(fahrenheit)
    logging.debug("Celsius temperature: %f", celsius)
    print(f"{fahrenheit:.1f} F is {celsius:.1f} C")
finally:  # cleanup
    print("ALL DONE")
