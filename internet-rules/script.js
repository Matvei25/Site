document.getElementById('showPythonResult').addEventListener('click', () => {
    // Запускаем Python скрипт
    const pythonScript = document.getElementById('pythonScript');
    
    pythonScript.run().then(result => {
        document.getElementById('output').textContent = result; // Выводим результат выполнения Python скрипта
    }).catch(err => {
        document.getElementById('output').textContent = 'Ошибка выполнения скрипта: ' + err;
    });
});
