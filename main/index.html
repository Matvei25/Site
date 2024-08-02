<?php
$directory = '.';
if (isset($_GET['dir'])) {
    $directory = $_GET['dir'];
}

if (isset($_POST['create_dir'])) {
    $newDir = $_POST['new_dir'];
    if (!empty($newDir)) {
        mkdir($directory . '/' . $newDir);
    }
}

if (isset($_POST['delete'])) {
    $itemToDelete = $_POST['item_to_delete'];
    if (is_dir($itemToDelete)) {
        rmdir($itemToDelete);
    } else {
        unlink($itemToDelete);
    }
}

$files = scandir($directory);
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Файловый менеджер</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Файловый менеджер</h1>
        <h2>Текущая директория: <?php echo htmlspecialchars($directory); ?></h2>

        <form method="POST">
            <input type="text" name="new_dir" placeholder="Имя новой папки" required>
            <button type="submit" name="create_dir">Создать папку</button>
        </form>

        <h3>Содержимое директории:</h3>
        <ul>
            <?php foreach ($files as $file): ?>
                <?php if ($file != '.' && $file != '..'): ?>
                    <li>
                        <?php if (is_dir($file)): ?>
                            <a href="?dir=<?php echo urlencode($directory . '/' . $file); ?>"><?php echo htmlspecialchars($file); ?></a>
                        <?php else: ?>
                            <?php echo htmlspecialchars($file); ?>
                        <?php endif; ?>
                        <form method="POST" style="display:inline;">
                            <input type="hidden" name="item_to_delete" value="<?php echo htmlspecialchars($directory . '/' . $file); ?>">
                            <button type="submit" name="delete">Удалить</button>
                        </form>
                    </li>
                <?php endif; ?>
            <?php endforeach; ?>
        </ul>
    </div>
</body>
</html>
