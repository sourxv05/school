function updateCities() {
            var countryDropdown = document.getElementById("country");
            var cityDropdown = document.getElementById("city");

            // Clear city dropdown
            cityDropdown.innerHTML = '';

            // Define city options based on the selected country
            var cities = {
                usa: ['New York', 'Los Angeles', 'Chicago'],
                canada: ['Toronto', 'Vancouver', 'Montreal']
                // Add more cities as needed
            };

            var selectedCountry = countryDropdown.value;
            var countryCities = cities[selectedCountry];

            if (countryCities) {
                for (var i = 0; i < countryCities.length; i++) {
                    var option = document.createElement('option');
                    option.value = countryCities[i];
                    option.text = countryCities[i];
                    cityDropdown.appendChild(option);
                }
            }
        }
