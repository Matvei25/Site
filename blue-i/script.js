function startEating() {
    const blueI = document.getElementById('blueI');
    
    // Переместить "i" к торту
    blueI.style.bottom = '200px'; // Двигаем "i" к торту

    // После задержки возвращаем "i" обратно
    setTimeout(() => {
        blueI.style.bottom = '150px'; // Возвращаем на место
        alert("Синий 'i' съел торт!"); // Сообщение о том, что торт съеден
    }, 1000);
}
