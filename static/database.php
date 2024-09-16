<?php
header('Content-Type: application/json');

// Database connection
$servername = "localhost";
$username = "root";  
$password = ""; 
$dbname = "face_recognition_db";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$page = isset($_GET['page']) ? intval($_GET['page']) : 1;
$limit = isset($_GET['limit']) ? intval($_GET['limit']) : 10;

$offset = ($page - 1) * $limit;

// Fetch records
$sql = "SELECT * FROM records LIMIT $limit OFFSET $offset";
$result = $conn->query($sql);

$records = [];
while ($row = $result->fetch_assoc()) {
    $records[] = $row;
}

// Check if there are more records
$sqlCount = "SELECT COUNT(*) AS count FROM records";
$resultCount = $conn->query($sqlCount);
$rowCount = $resultCount->fetch_assoc();
$hasMoreRecords = $rowCount['count'] > $offset + $limit;

$response = [
    'records' => $records,
    'hasMoreRecords' => $hasMoreRecords
];

echo json_encode($response);

$conn->close();
?>
