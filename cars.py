#!/usr/bin/env python3

import json

cars = {
	"manufacturers": [
		"Cadillac", "Chevrolet", "BMW"
	]
}

print(json.dumps(cars, indent=4))