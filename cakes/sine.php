<?php
// Получаем текущий URL страницы
$currentUrl = "http://" . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
echo "Ссылка на страницу: " . $currentUrl;
?>
