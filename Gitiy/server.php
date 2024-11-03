<?php
// Пример простого PHP скрипта для обработки сообщений
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $message = $_POST['message'];
    // Здесь можно добавить код для сохранения сообщения в базу данных
    echo json_encode(['status' => 'success', 'message' => $message]);
}
?>
