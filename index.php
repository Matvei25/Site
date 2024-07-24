echo "PHP is working"
<?php
$nonsenseArray = [
    "Летучие свиньи",
    "Зеленые облака",
    "Космические бананы",
    "Танцующие кактусы",
    "Молоко из радуги"
];

header('Content-Type: application/json');
echo json_encode($nonsenseArray);
?>
