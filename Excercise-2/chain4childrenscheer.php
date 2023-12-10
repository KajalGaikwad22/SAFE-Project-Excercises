<?php
$host = "localhost";
$port = "5432";  // Default PostgreSQL port
$dbname = "PDdb";
$user = "postgres";
$password = "Kajal@701";

try {
    $conn = new PDO("pgsql:host=$host;port=$port;dbname=$dbname;user=$user;password=$password");
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Select all data from the table
    $sql = "SELECT * FROM chain_members";
    $result = $conn->query($sql);

    // Display members
    echo "<h2>Chain Members</h2>";
    if ($result->rowCount() > 0) {
        while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
            echo "ID: " . $row["id"]. " - Name: " . $row["name"]. " - Email: " . $row["email"]. "<br>";
        }
    } else {
        echo "0 results";
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}

$conn = null;
?>
