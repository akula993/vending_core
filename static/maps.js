
        var resultsElement = document.getElementById('results');
        var valuesString = resultsElement.dataset.values; // Получение значения атрибута data-values
        var valuesArray = valuesString.split(','); // Разбивка строки на массив значений

        // Удаляем последний элемент массива, так как он будет содержать пустую строку
        valuesArray.pop();

        // Получение данных для меток (labels) и значений (data) из массива значений
        var labels = [{% for counter in machine.counter.all %}'{{ counter.month|date:"d-m-yг" }}',{% endfor %}];
        var data = valuesArray.map(function (value) {
            return parseInt(value); // Парсим значения в числа, если они являются числами
        });
        var reversedData = data.slice().reverse();
        var result = data.map(function (curr, index) {
            if (index === 0) {
                return curr;
            } else {
                return data[index - 1] - curr;
            }
        });


        data = result.map(s => Math.abs(s));

        data = data.map(
            function (n) {
                return (n * 10);
            }
        );
        console.log(data.shift());
        var counterData = {
            labels: labels,
            datasets: [{
                label: 'Значение счетчика',
                data: data,
                fill: false,
                borderColor: 'rgba(75, 192, 192, 1)',
                tension: 0.1
            }]
        };
        var counterConfig = {
            type: 'line',
            data: counterData,
            options: {
                responsive: true,
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Дата и время'
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Значение счетчика'
                        }
                    }
                }
            }
        };
        var counterChart = new Chart(document.getElementById('counterChart'), counterConfig);