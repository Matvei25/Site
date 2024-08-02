document.getElementById('sineButton').addEventListener('click', function() {
    fetch('sine.php')
        .then(response => response.text())
        .then(data => {
            document.getElementById('sine').innerText = data;
        })
        .catch(error => console.error('Ошибка:', error));
});
