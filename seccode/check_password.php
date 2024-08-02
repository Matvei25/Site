<?php
$secret_password = '2590178643';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input_password = $_POST['password'] ?? '';

    if ($input_password === $secret_password) {
        echo 'success';
    } else {
        echo 'fail';
    }
}
?>
