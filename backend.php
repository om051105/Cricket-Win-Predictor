<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $team1 = $_POST["team1"];
    $team2 = $_POST["team2"];

    // Call Python ML Model
    $command = escapeshellcmd("python3 predict.py " . escapeshellarg($team1) . " " . escapeshellarg($team2));
    $output = shell_exec($command);

    // Send Response
    echo json_encode(["team1" => $team1, "team2" => $team2, "winChance" => $output]);
}
?>
