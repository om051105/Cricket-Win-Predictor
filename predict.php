<?php
if (isset($_POST['team1']) && isset($_POST['team2'])) {
    $team1 = escapeshellarg($_POST['team1']);
    $team2 = escapeshellarg($_POST['team2']);

    // Run Python script
    $output = shell_exec("python3 predict.py $team1 $team2");

    // Send response
    echo nl2br($output);
}
?>